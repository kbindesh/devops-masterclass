# Install and Configure AWS CLI utility

## 01. Install AWS CLI tool

Kindly refer this official documentation link for downloading and installing AWS CLI tool: </br>
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

- In order to make sure that the installation was successful, kindly launch terminal/command prompt/powershell prompt and run the following command:

```
# After installing AWS CLI, check aws cli version on terminal
aws --version
```

## 02. Connect to an AWS Account using AWS CLI

### 2.1 Create an AWS IAM User and generate the access and secret keys

- Navigate to AWS Management Console >> IAM >> Users >> Create User
  - **Name**: awscliuser
  - **Provide user access to the AWS Management Console**: Disable
  - **Attach policies directly**: AdministratorAccess

- Now, open the user (e.g. awscliuser) detail page >> Security credentials >> Access keys >> Create access key
  - Download the generated keys in .csv format

### 2.2 Configure IAM User Access keys on local system

- Switch to your local system and open the terminal/command prompt and run the following commands to configure the AWS credentials for above created user and access AWS resources using AWS CLI commands:

```
# Connect to your AWS Account using AWS CLI
aws configure

[Enter Access Key, Secret Access Key, Region and Output format (text/json) when prompted]

# To check if authentication is working, try querying something from your account using AWS CLI
aws s3 ls
OR
aws iam list-users

[The preceding command should return user lists from your AWS account]
```

## 03. Reference

- AWS CLI Installation
  - https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
- AWS CLI Command Reference
  - https://docs.aws.amazon.com/cli/latest/
