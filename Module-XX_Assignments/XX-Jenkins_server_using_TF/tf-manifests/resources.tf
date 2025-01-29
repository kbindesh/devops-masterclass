resource "aws_instance" "linux_server" {
  depends_on             = [aws_security_group.jenkinsserver_sg]
  ami                    = data.aws_ami.amz_lnx2_ami.id
  instance_type          = var.jenkinsserver_instance_type
  key_name               = var.jenkinsserver_kp
  vpc_security_group_ids = [aws_security_group.jenkinsserver_sg.id]
  user_data              = file("${path.module}/scripts/jenkins_install.sh")

  tags = {
    Name = var.servername_var
    OS   = "Linux"
  }
}

resource "aws_security_group" "jenkinsserver_sg" {
  name   = var.jenkinsserver_sg_name
  vpc_id = data.aws_vpc.vpc_id.id
}

resource "aws_security_group_rule" "jenkins_sg_ingress_rule" {
  description       = "Allow Jenkins traffic for public"
  type              = "ingress"
  from_port         = 8080
  to_port           = 8080
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.jenkinsserver_sg.id
}

resource "aws_security_group_rule" "ssh_sg_ingress_rule" {
  description       = "Allow SSH traffic for public"
  type              = "ingress"
  from_port         = 22
  to_port           = 22
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.jenkinsserver_sg.id
}

resource "aws_security_group_rule" "sg_egress_rule" {
  description       = "Allow all traffic to internet"
  type              = "egress"
  from_port         = 0
  to_port           = 0
  protocol          = "-1"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.jenkinsserver_sg.id
}
