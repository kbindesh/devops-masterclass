# Introducing AWS SDK (Boto3)

## 01. What is Boto3?

- Boto3 is the Amazon Web Services (AWS) SDK for Python.
- It enables Python developers to create, configure, and manage AWS services, such as EC2 and S3. Boto3 provides an easy-to-use, object-oriented API, as well as low-level access to AWS services.
- Boto3 is built on the top of a library called Botocore, which the AWS CLI shares.
- Botocore provides the low-level clients, session and credentials, and configuration data. Boto3 built on the top of Botocore by providing its own session, resources, collections, waiters, and paginators.

## 02. Setting-up system for Boto3

### 2.1: Installing Boto3 & AWS CLI

```
# Windows users
pip install boto3

# Linux users
pip3 install boto3 --user

# Install AWS CLI
sudo pip install awscli

```

### 2.2 Connect to AWS Account

```
aws configure

[Enter the requested keys, region and format details]
```

## 03. Working with Boto3

```
# import the boto3 package
import boto3

# Create boto3 client for ec2 service
client = boto3.client('ec2')

# Create boto3 client for 3 service
client = boto3.client('s3')
```

## 04. Sample code

### 4.1: Describe Regions and Availability Zones

```
ec2 = boto3.client('ec2')

# Retrieves all regions/endpoints that work with EC2
response = ec2.describe_regions()
print('Regions:', response['Regions'])

# Retrieves availability zones only for region of the ec2 object
response = ec2.describe_availability_zones()
print('Availability Zones:', response['AvailabilityZones'])
```

### 4.2: Describe security groups

```
ec2 = boto3.client('ec2')

try:
    response = ec2.describe_security_groups(GroupIds=['SECURITY_GROUP_ID'])
    print(response)
except ClientError as e:
    print(e)
```

### 4.3: Create a Security group with rules

```
ec2 = boto3.client('ec2')

response = ec2.describe_vpcs()
vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')

try:
    response = ec2.create_security_group(GroupName='SECURITY_GROUP_NAME',
                                         Description='DESCRIPTION',
                                         VpcId=vpc_id)
    security_group_id = response['GroupId']
    print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))

    data = ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {'IpProtocol': 'tcp',
             'FromPort': 80,
             'ToPort': 80,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp',
             'FromPort': 22,
             'ToPort': 22,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
        ])
    print('Ingress Successfully Set %s' % data)
except ClientError as e:
    print(e)
```

### 4.4: Delete a Security group

```
ec2 = boto3.client('ec2')

# Delete security group
try:
    response = ec2.delete_security_group(GroupId='SECURITY_GROUP_ID')
    print('Security Group Deleted')
except ClientError as e:
    print(e)
```

### 4.5: Create an EC2 Instance

- https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/create_instances.html

```
import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId='ami-5eb63a32',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
)
print(instance[0].id)
```

### 4.6: Describe instances

```
response = client.describe_instances(
    InstanceIds=[
        'string',
    ],
    DryRun=True|False,
    Filters=[
        {
            'Name': 'string',
            'Values': [
                'string',
            ]
        },
    ],
    NextToken='string',
    MaxResults=123
)
```

### 4.6: Stop instances

```
response = client.start_instances(
    InstanceIds=[
        'string',
    ],
    AdditionalInfo='string',
    DryRun=True|False
)
```

### 4.7: Create a S3 bucket

```
import logging
import boto3
from botocore.exceptions import ClientError


def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True
```

### 4.8: List buckets

```
s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
```
