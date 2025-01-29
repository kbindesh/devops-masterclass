#!/bin/bash
yum update -y
yum install -y httpd
systemctl enable httpd
service httpd start  
echo '<h1>Terraform is Awesome..</h1>' | sudo tee /var/www/html/index.html
mkdir /var/www/html/app1
echo '<!DOCTYPE html> <html> <body style="background-color:rgb(250, 210, 210);"> <h1>Welcome to Terraform Bootcamp</h1> <p>Learn Terraform with Bindesh</p> <p>Application Version: v1</p> </body></html>' | sudo tee /var/www/html/app1/index.html
curl http://169.254.169.254/latest/dynamic/instance-identity/document -o /var/www/html/app1/metadata.html