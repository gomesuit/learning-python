import boto3

ec2 = boto3.client('ec2')

instances = ec2.describe_instances()

no_tags = []
for reservation in instances['Reservations']:
    keys = [tag['Key'] for tag in reservation['Instances'][0]['Tags']]
    if 'project' not in keys:
        no_tags.append(reservation['Instances'][0]['InstanceId'])

print(no_tags)
