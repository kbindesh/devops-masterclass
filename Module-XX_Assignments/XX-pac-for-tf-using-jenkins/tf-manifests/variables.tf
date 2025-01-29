variable "webserver_sg_name" {
  type    = string
  default = "webserver-sg"
}

variable "web_sg_ingress_rule_from_port" {
  type    = number
  default = 22
}

variable "web_sg_ingress_rule_to_port" {
  type    = number
  default = 22
}

variable "web_sg_ingress_rule_protocol" {
  type    = string
  default = "tcp"
}

variable "web_sg_ingress_rule_cidr" {
  type    = list(string)
  default = ["0.0.0.0/0"]
}
