from __init__ import *

from aws_costing import *

import pytz

from datetime import datetime

#Database Connection

import psycopg2

con = psycopg2.connect(host=HOST_NAME, dbname=DB_NAME, user=DB_USER, password=DB_USER_PASSWORD, port=5432)

cur = con.cursor()

def rule (instance_type, iname):

    """
        This Function is to check if the Instance is Right sized based on its Name. 
        :param instance_type: Describes Type and Size of AWS Instance 
        :param iname: Name of the AWS Instance (if specified else None) 
        :return: 0 if the instance is right sized in accordance with name 
            else 1
    """

    if ('ims' in iname.lower()) or ('gateway' in iname.lower()) or ('gw' in iname.lower()) or ('dm' in iname.lower()):
        if instance_type.endswith('.xlarge') or (instance_type.endswith('.large')) or (instance_type.endswith('.medium')) or (instance_type.endswith('.small')) or (instance_type.endswith('.micro')):

            return 0
        else:
            return 1

    elif 'crs' in iname.lower():
        if (instance_type.endswith('.4xlarge')) or (instance_type.endswith('.2xlarge')) or (instance_type.endswith('.xlarge')) or (instance_type.endswith('.large')) or (instance_type.endswith('.medium')) or (Instance_type.endswith('.small')) or (instance_type.endswith('.micro')):
            return 0
        else:
            return 1

    elif 'rm' in iname.lower():
        if instance_type.endswith('.2xlarge') or (instance_type.endswith('.xlarge')) or (instance_type.endswith('large')) or (instance_type.endswith('.medium')) or (instance_type.endswith('.small')) or (instance_type.endswith('micro')):
            return 0
        else:
            return 1
    else:
        if (instance_type.endswith('.xlarge')) or (instance_type.endswith('.large')) or (instance_type.endswith('.medium')) or (instance_type.endswith('.small')) or (instance_type.endswith('.micro')):
            return 0
        else:
            return 1

def aws_all_instances():

    """
        This Function is to get information about all Instances in AWS and store it in DB for Cleanup and
        Reporting purpose.

        :return:
    """
    #Query to insert

    sql_query="""INSERT INTO aws_instances (instance_Id, instance_Name, owner, purpose, state, state_transistion_time, Age, DND, YEB, Instance_Type, Type_Violation, Architecture, Image_id, private_ip, public_ip, virtualization_type,vpc_id, Region, Cost_saved) VALUES (%s, %s,%s,%s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    sg_query = """INSERT INTO aws_security_groups (SecurityGroup_Id, SecurityGroup_Name, Instance_Id, Instance_Name, owner, public_ip, Region)VALUES (%s, %s, %s, %s, %s, %s, %s)"""


    #Iterating through all regions for getting all Instances

    for region in region_list:
        ec2_res = boto3.resource('ec2', aws_access_key_id=AWS_ACCESS_ID, aws_secret_access_key=AWS_ACCESS_KEY,region_name=region, verify=False)

        for instance in ec2_res.instances.all():
            try:
                print("----------------------------------------------------------------------------------------------")
                i_id=instance.id #Instance Id in AWS
                tags= make_tag_dict(instance) #Dictionary of Tags for a Instance
                i_name="None" #Instance Name
                i_owner="None" #Instance Owner name
                i_purpose="None" #Instance purpose
                if (ResourceName in tags) or ('NAME' in tags):
                    i_name=tags.get(ResourceName) or tags.get("NAME")
                if (ResourceOwner in tags) or ('OWNER' in tags):
                    i_owner=tags.get(ResourceOwner) or tags.get("OWNER")
                if (ResourcePurpose in tags) or ('PURPOSE' in tags):
                    i_purpose=tags.get(ResourcePurpose) or tags.get("PURPOSE")

                i_state=instance.state.get("Name")  #Instance State: Running or Stopped
                #DND tag of Instance if present
                i_tag_dnd=tags.get(dnd_tag, 0)
                #YEB tag of Instance if present
                i_tag_infra=tags.get(infra_tag, 0)
                i_type=instance.instance_type #Instance type and size : e.g. General purpose and .xlarge
                viol=rule(i_type, i_name) #Check Instance is of right Size
                i_architecture=instance.architecture #Instance architecture
                i_image=instance.image_id #Instance image id associated with it
                private_ip=instance.private_ip_address #Instance private IP address
                public_ip=instance.public_ip_address#Instance public IP address
                i_virtual_type=instance.virtualization_type #Instance virtualization Type
                i_vpc=instance.vpc_id #Instance Virtual Private Cloud(VPC) Id

                try:
                    for sg in instance.security_groups:
                        security_group=ec2_res.SecurityGroup(sg.get("GroupId"))
                        sg_viol=0

                        for ip in security_group.ip_permissions:
                            if '0.0.0.0/0' in str(ip.get("IpRanges")):
                                sg_viol=1
                            if sg_viol==1:
                                print("sg_id: " + security_group.group_id)
                                print("sg_name: " + security_group.group_name)
                                print("ins_id: " +i_id +"\ni_name: "+i_name)
                                cur.execute(sg_query, (security_group.group_id, security_group.group_name, i_id, i_name,i_owner, public_ip, region))
                except Exception as exc:
                    print(exc)

                #Printing all details for log

                print(" I_id: "+str(i_id) +"name: " + str(i_name) +" owner: "+ str(i_owner)+ "state: "+str(i_state)+" DND: "+str(i_tag_dnd) + "type: "+str(i_type) + "architecture: "+str(i_architecture) +"Image-id: "+ str(i_image) + "private_ip: "+str(private_ip) +"public: "+ str(public_ip)+" virtualization: "+str(i_virtual_type) + " vpc: " +str(i_vpc))

                try:
                    #Time when Instance changed its State
                    state_transition_time = parse(instance.state_transition_reason, fuzzy=True)
                    state_transition_time =state_transition_time.replace(tzinfo=pytz.utc)
                    print("state_transition: " + str(state_transition_time))
                    launch_time=instance.launch_time.replace(tzinfo=pytz.utc)
                    print("launch time: " + str(launch_time))
                except ParserError:
                    #if transition time is not present then use instance last launch time(run time)
                    launch_time=instance.launch_time.replace(tzinfo=pytz.utc)
                    print("launch time; " + str(launch_time))
                    state_transition_time=launch_time
                    print("state_transition: " + str(state_transition_time))
                i_age = (today - state_transition_time).days # Time for which Instance is in a particular state
                if i_age < 0:
                    i_age = 0
                print("i_age: " + str(i_age))

                #i_cost saved: cost we save if we stop this Instance now
                #price: per hour cost of Instance

                i_cost_saved, price=ins_per_hour_cost (instance, region)
                i_cost_saved = round(i_cost_saved, 2)
                #i_cost_saved=0.0
                cur.execute(sql_query, (i_id, i_name, i_owner, i_purpose, i_state, state_transition_time, i_age, i_tag_dnd,i_tag_infra, i_type, viol, i_architecture, i_image, private_ip, public_ip, i_virtual_type, i_vpc, region, i_cost_saved))

            except Exception as exc:
                print(exc)

def aws_all_volumes():
    """
    This function is to get info about all volumes in AWS 

    :return:
    """
    sql_query="""INSERT INTO aws_volumes(Volume_Id,Volume_Name,Owner,State,State_transistion_time,Age,DND,viol,Volume_Type,Volume_Size,Region,Cost_Saved) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    #Iterating over all regions
    ec2_res=boto3.resource('ec2',aws_access_key_id=AWS_ACCESS_ID , aws_secret_access_key=AWS_ACCESS_KEY,region_name=region,verify=False)

    #Cloudtrail service keeps log of all activities related to a particular resource
    cloudtrail=boto3.resource('cloudtrail',aws_access_key_id=AWS_ACCESS_ID , aws_secret_access_key=AWS_ACCESS_KEY,region_name=region,verify=False)
    for volume in ec2_res.volume.all():
        try:
            print("---------------------------------------------------------------------------------------")
            vol_id=volume.id
            vol_type=volume.type
            vol_size=volume.size
            vol_name="None"
            vol_owner="None"
            tags=make_tag_dict(volume)

            if (ResourceName in tags) or (ResourceName.lower() in tags) or ('NAME' in tags):
                vol_name=tags.get(ResourceName) or tags.get(ResourceName.lower()) or tags.get('NAME')
            if (ResourceOwner in tags) or (ResourceOwner.lower() in tags) or ('OWNER' in tags):
                vol_owner=tags.get(ResourceOwner) or tags.get(ResourceOwner.lower()) or tags.get('OWNER')

            if dnd_tag in tags:
                dnd=tags.get('DND')
            else:
                dnd= " "
            state= volume.state

            attrlist = [{'AttributeKey' : 'ResourceName','AttributeValue':volume.id}]
            resource = cloudtrail.lookup_events(LookupAttributes=attrlist,StartTime=today-timedelta(days=90) , MaxResults =5)

            if response['Events']:
                e= response['Events']
                state_transistion_time = e[0]['EventTime']
                if e[0]['EventName']=='DetachVolume':
                    viol=0
                else:
                    viol=1
            else:
                state_transistion_time = volume.create_time
                viol=0
            vol_age=(today-state_transistion_time).days
            vol_cost_saved=0
            if vol_age > days_limits_to_delete_vol:
                vol_cost_saved = aws_vol_per_month_cost(volume,region)

            print("Id: "+str(vol_id)+" name: "+str(vol_name)+" owner: "+str(vol_owner)+" state: "+str(state)+" time: "+str(state_transistion_time)+" dnd: "+str(dnd)+" viol: "+str(viol)+" type: "+str(vol_type)+" region: "+str(region)+" cost: "+str(vol_cost_saved))

            cur.execute(sql_query,(vol_id,vol_name,vol_owner,state,state_transistion_time,vol_age,dnd,viol,vol_type,vol_size,region,vol_cost_saved))
        except Exception as exc:
            print(exc)

def aws_snapshots():

    sql_query="""INSERT INTO aws_snapshots (Snapshot_Id,Snapshot_Name,Snapshot_Desc,Owner,State,Created_time,Age,DND,Snapshot_Size,Region,Cost_Saved) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    for region in region_list:
        ec2_res=boto3.resource('ec2',aws_access_key_id=AWS_ACCESS_ID , aws_secret_access_key=AWS_ACCESS_KEY,region_name=region,verify=False)
        snapshots=ec2_res.snapshots.filter(OwnerIds=['self'])

        for snapshot in snapshots:
            try:
                print("---------------------------------------------------------------------------------------")
                snap_id=snapshot.id
                snap_desc=snapshot.description
                snap_state=snapshot.state
                snap_owner=snapshot.owner_id
                snap_size=snapshot.volume_size
                snap_name="None"
                tags=make_tag_dict(snapshot)
                if (ResourceName in tags) or (ResourceName.lower() in tags) or ('NAME' in tags):
                    snap_name=tags.get(ResourceName) or tags.get(ResourceName.lower()) or tags.get('NAME')
                if (ResourceOwner in tags) or (ResourceOwner.lower() in tags) or ('OWNER' in tags):
                    snap_owner=tags.get(ResourceOwner) or tags.get(ResourceOwner.lower()) or tags.get('OWNER')

                if dnd_tag in tags:
                    dnd=tags.get('DND')
                else:
                    dnd= " "
                created_time=snapshot.start_time
                snap_age=(today-created_time).days
                snap_cost_saved=0
                if snap_age > days_limit_to_delete_snapshot:
                    if 'rehearsals' not in snapshot.description.lower():
                        snap_cost_saved = snap_get_cost_saving(snap_size,region)
                print("Id: "+str(snap_id)+" name: "+str(snap_name)+" owner: "+str(snap_owner)+" state: "+str(snap_state)+" time: "+str(created_time)+" dnd: "+str(dnd)+" region: "+str(region)+" cost: "+str(snap_cost_saved))
                cur.execute(sql_query,(snap_id,snap_name,snap_desc,str(snap_owner),snap_state,created_time,snap_age,dnd,snap_size,region,snap_cost_saved))
            except Exception as exc:
                print(exc)

def aws_amis():
    sql_query="""INSERT INTO aws_amis(Image_Id,Image_Name,Image_Desc,Owner,State,Created_Time,Age,DND,Image_Type,Region) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    for region in region_list:
        ec2_res=boto3.resource('ec2',aws_access_key_id=AWS_ACCESS_ID , aws_secret_access_key=AWS_ACCESS_KEY,region_name=region,verify=False)
        amis=ec2_res.images.filter(Owners=['self'])

        for ami in amis:
            try:
                print("---------------------------------------------------------------------------------------")
                if ami.description is not None:
                    ami_desc = ami.description
                else:
                    ami_desc= " "
                ami_owner=ami.owner_id
                ami_type=ami.image_type
                tags=make_tag_dict(ami)
                if (ResourceOwner in tags) or (ResourceOwner.lower() in tags) or ('OWNER' in tags):
                    ami_owner=tags.get(ResourceOwner) or tags.get(ResourceOwner.lower()) or tags.get('OWNER')
                if dnd_tag in tags:
                    dnd=tags.get(dnd_tag)
                else:
                    dnd= " "
                created_time=ami.creation_time
                created_time=datetime.strptime(created_time,'%Y-%m-%dT%H:%M:%S:%fZ').replace(tzinfo=pytz.utc)
                ami_age=(today- created_time).days

                print(ami)

                cur.execute(sql_query,(ami.id,ami.name,ami_desc,str(ami_owner),ami.state,created_time,ami_age,dnd,ami_type,region))
            except Exception as exc:
                print(exc)



if __name__=="__main__":
    aws_all_instances()
    #aws_all_volumes()
    #aws_amis()
    #aws_snapshots()
    con.commit()
    cur.close()
    con.close()

print("******************************************************************************")
print("getting data in AWS DB at:" +str(datetime.now(tz=pytz.timezone('Asia/Kolkata'))))
print("******************************************************************************")






    








