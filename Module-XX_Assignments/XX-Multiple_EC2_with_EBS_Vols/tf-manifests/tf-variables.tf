variable "ec2_instance_count" {
  type    = number
  default = 1
}

variable "ec2_instance_type" {
  type    = string
  default = "t2.micro"
}

variable "ebs_vol_count" {
  type    = number
  default = 1
}

# Add more EBS volume sizes depending upon the no. of volumes 
variable "ebs_volume_sizes" {
  type    = list(any)
  default = [10]
}

# Add more EBS volume sizes depending upon the no. of volumes 
variable "ec2_device_names" {
  type    = list(any)
  default = ["/dev/sdd"]
}
