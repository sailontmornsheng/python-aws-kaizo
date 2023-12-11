import boto3
import pandas as pd

def get_user_input():
    access_key = input("Enter your AWS Access Key: ")
    secret_key = input("Enter your AWS Secret Key: ")
    region = input("Enter your AWS Region: ")

    return access_key, secret_key, region

def get_running_instances(access_key, secret_key, region):
    ec2 = boto3.client('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region)

    try:
        response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
        instances = response['Reservations']

        if instances:
            instance_data = []
            for reservation in instances:
                for instance in reservation['Instances']:
                    instance_id = instance['InstanceId']
                    state = instance['State']['Name']
                    public_ip = instance.get('PublicIpAddress', 'N/A')
                    private_ip = instance.get('PrivateIpAddress', 'N/A')

                    instance_data.append({
                        'Instance ID': instance_id,
                        'State': state,
                        'Public IP': public_ip,
                        'Private IP': private_ip
                    })

            df = pd.DataFrame(instance_data)
            file_name = f'running_instances_{region}.xlsx'
            df.to_excel(file_name, index=False)
            print(f"Data exported to {file_name}")
        else:
            print("No running instances found.")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    print("AWS EC2 Instance Fetcher\n")

    access_key, secret_key, region = get_user_input()

    print("\nFetching running EC2 instances...\n")

    get_running_instances(access_key, secret_key, region)

if __name__ == "__main__":
    main()
