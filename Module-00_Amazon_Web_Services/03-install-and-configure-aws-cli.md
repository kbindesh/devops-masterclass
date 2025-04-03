# Install and Configure AWS CLI utility

Kindly follow this official documentation link: </br>
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

```
# After installing AWS CLI, check aws cli version on terminal
aws --version

# Connect to your AWS Account using AWS CLI
aws configure

[Enter Access Key, Secret Access Key, Region and Output format (text/json) when prompted]

# To check if authentication is working, try querying something from your account using AWS CLI
aws s3 ls
OR
aws iam list-users
```
