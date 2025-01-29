# Data source for fetching Amazon Linux 2 AMI ID | us-east-1 region
data "aws_ami" "amz_lnx2_ami" {
  most_recent = true
  owners      = ["amazon"]
  filter {
    name   = "name"
    values = ["amzn2-ami-kernel-5.10-hvm-2.0.20240306.2-x86_64-gp2"]
  }
}

# Data source for fetching Default VPC (existing) arguments
data "aws_vpc" "vpc_id" {
  tags = {
    "Name" = "Default VPC - DO NOT DELETE"
  }
}
