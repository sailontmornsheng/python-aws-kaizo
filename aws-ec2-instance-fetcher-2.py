import subprocess
import json
import boto3
import openpyxl
from botocore.exceptions import ProfileNotFound
from datetime import datetime

def fetch_aws_config():
    try:
        aws_config = subprocess.check_output(['aws', 'configure', 'list']).decode('utf-8')
        return aws_config
    except subprocess.CalledProcessError:
        return None

def ask_user_for_profile():
    aws_config = fetch_aws_config()
    if aws_config:
        profiles = [line.split()[1] for line in aws_config.split('\n') if line.startswith('profile')]
        print("Available AWS Profiles:")
        for profile in profiles:
            print(f" - {profile}")
        return input("Enter the profile you want to use: ")
    else:
        return None

def ask_user_for_credentials():
    access_key = input("Enter your AWS Access Key: ")
    secret_key = input("Enter your AWS Secret Key: ")
    return access_key, secret_key

def create_aws_session(profile=None, access_key=None, secret_key=None):
    try:
        if profile:
            session = boto3.Session(profile_name=profile)
        else:
            session = boto3.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key)
        return session
    except ProfileNotFound:
        print("Error: AWS CLI profile not found.")
        return None

def get_ec2_instances(session, region='all'):
    if region == 'all':
        regions = [region['RegionName'] for region in session.client('ec2').describe_regions()['Regions']]
    else:
        regions = [region]
    
    instances = []

    for region in regions:
        ec2 = session.client('ec2', region_name=region)
        response = ec2.describe_instances()
        
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instances.append({
                    'Name': get_tag_value(instance, 'Name'),
                    'InstanceId': instance['InstanceId'],
                    'State': instance['State']['Name'],
                    'InstanceType': instance['InstanceType'],
                    'Region': region,
                    'SecurityGroups': [sg['GroupName'] for sg in instance.get('SecurityGroups', [])],
                    'KeyPair': instance.get('KeyName', 'N/A')
                })

    return instances

def get_tag_value(instance, tag_key):
    for tag in instance.get('Tags', []):
        if tag['Key'] == tag_key:
            return tag['Value']
    return 'N/A'

def output_to_excel(instances, region):
    date_str = datetime.now().strftime('%Y%m%d')
    filename = f"ec2_instances_{region}_{date_str}.xlsx"
    
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    headers = ['Instance Name', 'Instance ID', 'State', 'Instance Type', 'Region', 'Security Groups', 'Associate Key Pair']
    sheet.append(headers)

    for instance in instances:
        row = [
            instance['Name'],
            instance['InstanceId'],
            instance['State'],
            instance['InstanceType'],
            instance['Region'],
            ', '.join(instance['SecurityGroups']),
            instance['KeyPair']
        ]
        sheet.append(row)

    workbook.save(filename)
    print(f"Data exported to {filename}")

def output_to_json(instances, region):
    date_str = datetime.now().strftime('%Y%m%d')
    filename = f"ec2_instances_{region}_{date_str}.json"
    
    with open(filename, 'w') as json_file:
        json.dump(instances, json_file, indent=2)
    print(f"Data exported to {filename}")

def main():
    profile = ask_user_for_profile()
    access_key, secret_key = None, None

    if not profile:
        access_key, secret_key = ask_user_for_credentials()

    session = create_aws_session(profile, access_key, secret_key)

    if session:
        region = input("Enter the AWS region to fetch EC2 instances (enter 'all' for all regions): ")
        instances = get_ec2_instances(session, region)

        for instance in instances:
            print(instance)

        output_format = input("Enter the output format (excel/json): ").lower()

        if output_format == 'excel':
            output_to_excel(instances, region)
        elif output_format == 'json':
            output_to_json(instances, region)
        else:
            print("Invalid output format. Please choose 'excel' or 'json'.")

if __name__ == "__main__":
    main()
