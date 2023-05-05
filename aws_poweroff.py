import boto3
import os
from __init__ import *
from aws_costing import *
import csv
import pytz
from datetime import datetime
from AwsUtils import get_instance_age


def aws_instance_stop():
    stopped_ins_cost_saving=0
    ins_count_on=0
    ins_count_off=0

    for region in region_list:
        ec2_res=boto3.resource('ec2',aws_access_key=AWS_ACCESS_ID,aws_secret_access_key=AWS_ACCESS_KEY,region_name=region,verify=False)
        running_instances=ec2_res.instances.filter(Filters=[{'Name':'instance-state-name','Values':['running']}])

        dnd_instances=ec2_res.instances.filter(Filters=[{'Name':f'tag:{dnd_tag}','Values':['1']}])
        print("DND Instances in "+str(region)+" :---------------------------------------------------------")
        for i in dnd_instances:
            print(i.id + "\t"+region)
        dnd_instances_lower=ec2_res.instances.filter(Filters=[{'Name':f'tag:{dnd_tag.lower()}','Values':['1']}])
        for i in dnd_instances.lower():
            print(i.id+"\t"+region)
        infra_instances=ec2_res.instances.filter(Filters=[{'Name':f'tag:{infra_tag}','Values':['1']}])
        print("Infra Instances "+str(region)+" :-----------------------------------------------")
        for i in infra_instances:
            print(i.id+"\t"+region)
        infra_instances_lower=ec2_res.instance.filter(Filters=[{'Name':f'tag:{infra_tag.lower()}','Values':['1']}])
        for i in infra_instances_lower:
            print(i.id+"\t"+region)

        print("Stopping instances in "+ str(region)+" :--------------------------------")
        for instance in running_instances:
            instance_id = instance.id
            print("Instance id is:"+instance_id)

            if instance in infra_instance or instance in infra_instance_lower:
                ins_count_on=ins_count_on +1
                continue
            if instance in dnd_instances or instance in dnd_instances_lower:
                ins_count_on=ins_count_on+1
                continue

            try:
                ins_age=get_instance_age(ec2_res,instance_id)

                print("ins age: "+str(ins_age)+" hrs limit to power off the instance is "+str(hours_limit_to_poweroff_ins))
                if ins_age < hours_limit_to_poweroff_ins:
                    ins_count_on=ins_count_on +1
                    continue
            except Exception as exc:
                print(exc)

            try:
                instance_id=instance.id
                cost_saved,ins_cost=ins_per_hour_cost(instance,region)
                instance.stop()

                stopped_ins_cost_saving=stopped_ins_cost_saving + (ins_cost *10)
                print(str(instance_id)+"\t"+region)
                ins_count_off=ins_count_off + 1
            except Exception as exc:
                print(exc)
    row=[stopped_ins_cost_saving]
    print("New ins cost saving by stopping operation: "+str(stopped_ins_cost_saving))
    with open(path +"saving/stop_ins_saving.csv","a+") as cw:
        csvwriter=csv.writer(cw,delimiter=',')
        csvwriter.writerow(row)
    print("No of instances still on" +str(ins_count_on))
    print("No of instances powered off "+str(ins_count_off))

if __name__=="__main__":
    aws_instances_stop()
    print("*******************************************************************")
    print("AWS shutdown at :" +str(datetime.now(tz=pytz.timezone('Asia/Kolkata'))))
    print("********************************************************************")

