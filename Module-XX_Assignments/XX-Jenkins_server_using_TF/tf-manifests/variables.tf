variable "jenkinsserver_ami_var" {
  type    = string
  default = "dummyami"
}

variable "jenkinsserver_instance_type" {
  type    = string
  default = "dummyinstancetype"
}

variable "jenkinsserver_kp" {
  type    = string
  default = "dummykeypair"
}

variable "servername_var" {
  type    = string
  default = "dummy-jenkinsserver"
}

variable "bucket_name" {
  type        = string
  description = "Bucket Name"
  default     = "bins3tflabbucket"
}

variable "env_type" {
  type    = string
  default = "DEV"
}

variable "jenkinsserver_sg_name" {
  type    = string
  default = "jenkinsserver-sg"
}
