from __init__ import *

pri_cli=boto3.client('pricing',aws_access_key_id=AWS_ACCESS_ID, aws_secret_access_key=AWS_ACCESS_KEY,region_name='ap-south-1',verify=False)

rem_days_in_month=(date(today.year,today.month,calendar.monthrange(today.year,today.month)[1]) - date(today.year,today.month,today.day)).days

rem_second_in_month=rem_days_in_month * seconds_in_day


def get_region_name(region_code):
    default_region = 'EU (Ireland)'
    endpoint_file=resource_filename('botocore','data/endpoints.json')
    try:
        with open(endpoint_file,'r') as f:
            data=json.load(f)
            region_desc = data['partitions'][0]['regions'][region_code]['description']
            return region_desc
    except IOError:
        return default_region


def ins_per_hour_cost(instance,region):
    region=get_region_name(region)
    ins_type=instance.instance_type

    flt='[{{"Field":"tenancy","Value":"shared","Type":"TERM_MATCH"}},'\
            '{{"Field":"operatingSystem","Value":"{o}","Type":"TERM_MATCH"}},'\
            '{{"Field":"preInstalledSw","Value":"NA","Type":"TERM_MATCH"}},'\
            '{{"Field":"location","Value":"{t}","Type":"TERM_MATCH"}},'\
            '{{"Field":"location","Value":"{r}","Type":"TERM_MATCH"}}]'

    f=flt.format(r=region,t=ins_type,o='Linux')
    data=pri_cli.get_products(ServiceCode='AmazonEC2',Filters=json.loads(f))
    od=json.loads(data['PriceList'][0])['terms']['OnDemand']
    id1=list(od)[0]
    id2=list(od[id1]['priceDimensions'])[0]
    ins_price=od[id1]['priceDimensions'][id2]['pricePerUnit']['USD']
    ins_price=float(ins_price)
    print("ins_per_hour_cost " +str(ins_price))
    cost_saved=ins_price * rem_days_in_month *24
    cost_saved=round(cost_saved,3)
    print("Cost saved is " +str(cost_saved))
    return cost_saved,ins_price


def aws_vol_per_month_cost(volume,region):
    region=get_region_name(region)
    volume_type=volume.volume_type
    volume_price = 0
    if volume_type=='sc1':
        volume_type= 'Cold HDD'
    elif volume_type =='st1':
        volume_type='Throughput Optimized HDD'
    elif volume_type =='io1':
        volume_type='Provisioned IOPS SSD'
    else:
        volume_type='General Purpose'

    storageData=pri_cli.get_products(
            ServiceCode='AmazonEC2',
            Filters=[
                {'Type':'TERM_MATCH','Field':'location','Value':region},
                {'Type':'TERM_MATCH','Field':'volumeType','Value':volume_type},
                ],maxResults=10)

    for storageVal in storageData["PriceList"]:
        storageValJson = json.loads(storageVal)
        if "OnDemand" in storageValJson["terms"] and len(storageValJson["terms"]["OnDemand"]) >0:
            for OnDemandValues in StorageValJson["terms"]["OnDemand"].keys():
                volume_price = (storageValJson["terms"]["OnDemand"][onDemandValues]["priceDimensions"][priceDimensionValues]["pricePerUnit"]['USD'])
                volume_price=float(volume_price)
                print("vol_per_month_cost "+str(volume_price))
                cost_saved=volume_price * float(volume.size) * (rem_seconds_in_month/2592000.00)
                print("cost saved is : "+str(cost_saved))
                cost_saved=round(cost_saved,3)
                return cost_saved
def snap_get_cost_saving(snap_size,region):
    if (region == 'us-east-1') or (region == 'us-east-2'):
        cost_saved = 0.05 *float(snap_size) *(rem_seconds_in_month/2592000.00)
    else:
        cost_saved= 0.053 * float(snap_size) * (rem_seconds_in_month/2592000.00)
    print("Snapshots cost saved "+str(cost_saved))
    cost_saved=round(cost_saved,3)
    return cost_saved



