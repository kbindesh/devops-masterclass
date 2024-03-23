variable "webserver_ami_var" {
  type    = string
  default = "dummyami"
}

variable "webserver_instance_type" {
  type    = string
  default = "dummyinstancetype"
}

variable "webserver_kp" {
  type    = string
  default = "dummykeypair"
}

variable "servername_var" {
  type    = string
  default = "dummy-webserver"
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

variable "webserver_sg_name" {
  type    = string
  default = "webserver-sg"
}
