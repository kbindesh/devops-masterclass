# Create an Amazon EC2 Instance using AWS CLI

To create an EC2 instance, you must have the following resources as a prerequisites:

- AMI (Amazon Machine Image)
- Key Pair
- Security Group
- VPC and a Subnet

### Step-01: Get the `Subnet ID` (manually)

- Navigate to VPC service dashboard >> Subnets >> Select the Subnet in which you want to create an EC2 instance >> Copy the **Subnet ID**

### Step-02: Get the AMI ID (manually)

- Navigate to EC2 service dashboard >> Images >> AMI Catalog >> Search any AMI >> select the AMI you want to use for launching an EC2 instance >> Copy the **AMI ID**

### Step-03: Create & Configure new `Security Group`

```
# AWS CLI command to create a security group | Replace the 'VPC ID' and 'Name' as per your requirement

aws ec2 create-security-group --group-name allow-ssh-sg --description "This SG is created using AWS CLI" --tag-specifications 'ResourceType=security-group,Tags=[{Key=Name,Value=allow-ssh-sg}]' --vpc-id "vpc-2e711a53"


# The preceding command execution will result in the following output
{
    "GroupId": "sg-013e389242f9e7895",
    "Tags": [
        {
            "Key": "Name",
            "Value": "allow-ssh-sg"
        }
    ]
}
```

- **Add a security group rule to the above created SG to allow SSH (port 22) Ingress traffic**

```
aws ec2 authorize-security-group-ingress --group-id "sg-013e389242f9e7895" --protocol tcp --port 22 --cidr "0.0.0.0/0" --tag-specifications 'ResourceType=security-group-rule,Tags=[{Key=Name,Value=allow-ssh-for-all}]'


# The preceding command execution will result in the following output
{
    "Return": true,
    "SecurityGroupRules": [
        {
            "SecurityGroupRuleId": "sgr-0bfefda2f930dcff4",
            "GroupId": "sg-013e389242f9e7895",
            "GroupOwnerId": "154511248558",
            "IsEgress": false,
            "IpProtocol": "tcp",
            "FromPort": 22,
            "ToPort": 22,
            "CidrIpv4": "0.0.0.0/0",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "allow-ssh-for-all"
                }
            ]
        }
    ]
}
```

### Step-04: Create a new `SSH Key Pair`

- The output key by default gets stored in ~/.ssh location.

```
aws ec2 create-key-pair --key-name  lnx-ec2-kp --query 'KeyMaterial' --output text > ~/.ssh/lnx-ec2-key
```

### Step-05: Create an `Amazon EC2 Instance`

- Now, as you have all the prerequisites in place for creating as EC2 instance, let's create one.

  - **AMI ID**: ami-0e826adbe998b4172 (amazon linux2 | x86_64)
  - **VPC ID**: vpc-2e711a53
  - **Subnet ID**: subnet-05341124
  - **Security Group ID**: sg-013e389242f9e7895
  - **Key Pair**: lnx-ec2-kp

- **Create a new file - [block-device-mapping.json](./scripts/block-device-mapping.json) for storing block device mapping settings for EC2 instance**:

```
[
  {
    "DeviceName": "/dev/sdf",
    "Ebs": {
      "VolumeSize": 20,
      "DeleteOnTermination": false
    }
  }
]
```

- **Create an EC2 Instance**

```
aws ec2 run-instances --image-id ami-0a9a48ce4458e384e --count 1 --instance-type t2.micro --key-name lnx-ec2-kp --security-group-ids sg-013e389242f9e7895 --subnet-id subnet-05341124 --block-device-mappings file://.\scripts\block-device-mapping.json --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=CLI-LAB-SERVER}]' 'ResourceType=volume,Tags=[{Key=Name,Value=cli-lab-server-disk}]'
```

### Step-06: Connect to the EC2 Instance (linux) over SSH

```
# Syntax - To initiate SSH connection, launch command prompt/terminal/powershell and run following command
ssh -i <home_dir>/.ssh/<key_pair_name> <target_machine_username>@<public_or_private_ip>

# Example
ssh -i C:\Users\ServerX\.ssh\lnx-ec2-key ec2-user@34.201.70.16
```

### Step-07: Terminate (delete) EC2 Instance | Delete other created resources

```
# Syntax
aws ec2 terminate-instances --instance-ids <ec2_instance_id>

# Example
aws ec2 terminate-instances --instance-ids i-0ce53550804d7d325

# Delete the above created SG
aws ec2 delete-security-group --group-name allow-ssh-sg

# Delete the above KeyPair
aws ec2 delete-key-pair --key-name lnx-ec2-kp
```
