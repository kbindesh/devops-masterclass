## Setting-up system for Boto3

1. Download and install Python
2. Install and configure AWS CLI
3. Install AWS SDK (Boto3)
4. Install IDE (VS Code)

### 2.1 Install Python

- You can download python from here: https://www.python.org/downloads/

```
# Check installed python version
python --version

# Check pip version
pip --version
OR
pip3 --version
```

### 2.2: Installing Boto3 & AWS CLI

```
# Windows users
pip install boto3

# Linux users
pip3 install boto3 --user

# Install AWS CLI
sudo pip install awscli

```

### 2.3 Connect to AWS Account

```
aws configure

[Enter the requested keys, region and format details]
```

### Query AWS Resources using AWS CLI

```
# Get the list of all the EC2 Instances
aws ec2 describe-instances

# Get the list of S3 Buckets
aws s3 ls
```
