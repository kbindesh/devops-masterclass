resource "aws_security_group" "webserver_sg" {
  name   = var.webserver_sg_name
  vpc_id = data.aws_vpc.vpc_id.id
}

resource "aws_security_group_rule" "http_sg_ingress_rule" {
  description       = "Allow HTTP traffic for public"
  type              = "ingress"
  from_port         = var.web_sg_ingress_rule_from_port
  to_port           = var.web_sg_ingress_rule_to_port
  protocol          = var.web_sg_ingress_rule_protocol
  cidr_blocks       = var.web_sg_ingress_rule_cidr
  security_group_id = aws_security_group.webserver_sg.id
}

resource "aws_security_group_rule" "sg_egress_rule" {
  description       = "Allow all traffic to internet"
  type              = "egress"
  from_port         = 0
  to_port           = 0
  protocol          = "-1"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.webserver_sg.id
}
