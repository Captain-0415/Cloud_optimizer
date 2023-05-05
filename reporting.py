from __init__ import *
import psycopg2

con = psycopg2.connect(host=HOST_NAME,dbname=DB_NAME,user=DB_USER,password=DB_USER_PASSWORD,port=5432)
cur=con.cursor()
aws_report=0
aws_report_data={}

aws_ins_data,aws_vol_data,aws_snap_data={},{},{}
aws_instance_csv_field=["InstanceId","InstanceName","Owner","PowerOnSince","Region"]
aws_volume_fields=["VolumeId","VolumeName","Owner","PowerOnSince","Region"]
aws_snapshots_fields=["SnapshotId","SnapshotName","SnapOwner","PowerOnSince","Region"]

fileformat = str(datetime.now().date())+".csv"

if is_feature_enabled('AWS_BASE'):
    from aws_resources import *

    aws_report = 1
    print("******************************************************************************")
    print("AWS Report details :")

    aws_report_data["aws_no_of_running_instances"],aws_report_data["aws_running_ins_list"],aws_report_data["aws_no_of_stopped_instances"],aws_report_data["aws_stopped_ins_list"]=db_aws_instances(cur)

    aws_report_data["aws_available_vol_cnt"],aws_report_data["aws_available_vol_size"]=db_aws_volumes(cur)
    aws_report_data["aws_no_of_snapshots"],aws_report_data["aws_total_snapshot_size"]=db_aws_snapshots(cur)

    aws_report_data["aws_sg_viol_list"]=db_aws_security_groups(cur)

    aws_ins_data = aws_active_instances(cur)
    write_data_to_csv(path+"aws_instances" +fileformat,aws_instance_csv_field,aws_ins_data)

    aws_vol_data=aws_volume(cur)
    write_data_to_csv(path +"aws_volumes"+fileformat,aws_volume_fields,aws_vol_data)

    aws_snap_data=aws_snapshot(cur)
    write_data_to_csv(path+"aws_snapshot"+fileformat,aws_snapshots_fields,aws_snap_data)

    print("********************************************************************************")


try:
    query="""Select aws_savings FROM daily_cost_saved WHERE savings_on = %s"""
    cur.execute(query,(str(today.date()),))
    rows=cur.fetchall()
    aws_cost_saving_today=rows[0][0]
except Exception as e:
    print(e)
    aws_cost_saving_today=0
try:
    cost_saving_today,cost_saving_till_date=get_cost_saving()
    cost_saving_today=round(cost_saving_today,2)
    cost_saving_till_date=round(cost_saving_till_date,2)
except Exception as e:
    cost_saving_today,cost_saving_till_date=0,0

file_loader=FileSystemLoader(path+'templates/')
env=Environment(loader=file_loader)
template=env.get_template('index_test.html')
reporting_time=datetime.now()
warning="""PLease delete unused resources.
Specify owner and dnd tags on your resources."""

output=template.render(warning=warnings,aws_report=aws_report,aws_report_data=aws_report_data,aws_cost_saving_today=aws_cost_saving_today,days_limit_running_ins=days_limit_running_ins,days_limit_stopped_ins=days_limit_stopped_ins,cost_saving_till_date=cost_saving_till_date,report_time=report_time)
from_email=EMAIL_FROM
to_email=EMAIL_TO

subject=" Cloud Resource Management tool report"

message=MIMEMultipart('alternative')
message['Subject']=subject
message['From']=from_email
message['To']=', '.join(to_email)

message.attach(MIMEText(output, "html"))

"""Email Attachment"""

filename="cloudtrim_"+str(datetime.now().date())+".xlsx"
attachment= open(path+"reports/"+filename,"rb")
p=MIMEBase('application','octet-stream')
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition',"attachment; filename = %s" %filename)
message.attach(p)

msgbody=message.as_string()

server=SMTP('localhost',25)
server.sendmail(from_email,to_email,msgbody)

server.quit()

con.commit()
cur.close()
con.close()

print("*********************************************************************")
print("Reporting at : "+str(datetime.now(tz=pytz.timezone('Asia/Kolkata'))))
print("********************************************************************")
