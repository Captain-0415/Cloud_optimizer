#--------------------AWS dependencies-----------------------

from botocore.exceptions import ClientError
import boto3
import urllib3

#--------------------other dependencies----------------------

import os
import calendar
import csv
import json
#from parser import ParserError
import pytz
from datetime import datetime, timedelta, timezone, date
from dateutil.parser import parse, ParserError
from pkg_resources import resource_filename

#--------------------Email------------------------------------


from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

EMAIL_FROM = 'cloud_optimizer@gmail.com'
EMAIL_TO=[]

#----------------template------------------------------------

from jinja2 import Environment, FileSystemLoader


# Ignore AWS region request warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


#-----------------Feature toggler----------------------------
features={
 "FTO_AWS_BASE":1,
 }
 
 
 #----------------Check feature toggle------------------------
 
def is_feature_enabled(feature_name):
 	is_enabled = features.get('FTO_'+str(feature_name))
 	return is_enabled
 	
if is_feature_enabled('AWS_BASE'):
    AWS_ACCESS_ID='AKIAT2DS7G2GOQEVGDLL'
    AWS_ACCESS_KEY='dJjRa1JCvQ/KL4xtaU/UC23C+4o7/OC6aq2Lw6t4'
 	
 	
#--------------Database configuration-------------------------

HOST_NAME='localhost'
DB_NAME='postgres'
DB_USER='postgres'
DB_USER_PASSWORD='postgres'

#AWS all regions list
region_list=["us-east-1","us-east-2","us-west-1","us-west-2","ap-south-1","ap-northeast-2",
	     "ap-southeast-1","ap-southeast-2","ap-northeast-1","ca-central-1","eu-central-1",
	     "eu-west-1","eu-west-2","eu-west-3","eu-north-1"]
	    
#Thresholds
hours_limit_to_poweroff_ins=2
days_limit_running_ins=2
days_limit_stopped_ins=3
days_limit_to_delete_vol=7
days_limit_to_delete_ami=7
days_limit_to_delete_snapshot=7
days_limit_to_delete_instances=7
days_limit_to_delete_blob=7
seconds_in_day=86400
days_limit_to_delete_dnd_snapshots=5
clean_dnd_tagged_snaps= False

today= datetime.now(tz=pytz.utc)+timedelta(minutes=15)

#Filepath
path='example'  #path to scripts

#Resource tags
ResourceName = "Name"
ResourceOwner = "Email"
ResourcePurpose = "Purpose"
dnd_tag = "DND" #tag which will allow resource to run without interruptions
infra_tag = "DNP" #tag for excluding the resources from the tool



def make_tag_dict(ec2_objects):
	"""
	This function iterates through tags of a resource and converts it to a dictionary for
	easy access.
	"""
	
	tag_dict ={}
	if ec2_objects.tags is None:
		return tag_dict
	for tag in ec2_objects.tags:
		tag_dict[tag['Key']]= tag['Value']
	return tag_dict
	
	
def write_data_to_csv(filename,fieldname,data):
	with open(filename, 'w') as csvfile:
		writer=csv.DictWriter(csvfile, fieldnames=fieldname)
		
		writer.writeheader()
		writer.writerows(data)
		
		
def get_cost_saving():
	"""
	This function is used to get today's cost saving and cost saved till today by cleanup and stopping process.
	
	:return: Tuple. 1)cost_saving_today = Cost saved by stopping and cleaning up resources today
			2)cost_saved_till_date
			
	"""
	
	data=[]
	#single file created for each month
	
	try:
		with open(path + "cloud_cost_saving_"+str(calender.month_name[datetime.now().month])+str(datetime.now().year)+".csv","r",encoding="utf-8",errors="ignore") as cw:
			reader=csv.reader(cw,delimiter=',')
			for row in reader:
				if row:
					columns =[row[0],row[1],row[2]]
					data.append(columns)
			last_row=data[-1]   #last entry in file
			cost_saving_today=last_row[0]   #1st column gives today's saved cost
			cost_saving_till_date=last_row[1] #2nd column gives cost saved till date
			cost_saving_today=float(cost_saving_today)
			cost_saving_till_date=float(cost_saving_till_date)
			
			return cost_saving_today,cost_saving_till_date
	
	except Exception as exc:
		print(exc)
		with open(path + "cloud_cost_saving_"+str(calender.month_name[datetime.now().month])+str(datetime.now().year)+".csv","a+") as cw:
			csvwriter=csv.writer(cw,delimiter=',')
			csvwriter.writerow(["Today's cost saving($)","Cost saving till date($)","Date"])
		cost_saving_today=0.0
		cost_saving_till_date=0.0
		return cost_saving_today,cost_saving_till_date
		
def set_cost_saving(saving_today, cost_saving_till_date):
	"""
	This function is used to update the file for each month with a cost for log and reporting purpose
	"""
	
	saving_today=round(saving_today , 3)
	cost_saving_till_date=round(cost_saving_till_date, 3)
	row =[saving_today, cost_saving_till_date+saving_today, datetime.now().date()]
	with open(path + "cloud_cost_saving_"+str(calender.month_name[datetime.now().month])+str(datetime.now().year)+".csv","a+") as cw:
		csvwriter=csv.writer(cw,delimiter=',')
		csvwriter.writerow(row)
		
			 
 
 
  


