data "aws_availability_zones" "available" {
  state = "available"
}

data "aws_ami" "amzn_lnx2_ami_ds" {
  most_recent = true
  owners      = ["amazon"]
  filter {
    name   = "name"
    values = ["amzn2-ami-kernel-5.10-hvm-2.0.20240306.2-x86_64-gp2"]
  }
}

data "aws_subnet" "ec2_subnet" {
  filter {
    name   = "tag:Name"
    values = ["deafult subnet 1a"]
  }
}
