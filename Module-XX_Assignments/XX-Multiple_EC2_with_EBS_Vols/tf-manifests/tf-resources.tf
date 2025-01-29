resource "aws_instance" "ec2_instances" {
  count             = var.ec2_instance_count
  ami               = data.aws_ami.amzn_lnx2_ami_ds.id
  instance_type     = var.ec2_instance_type
  availability_zone = data.aws_availability_zones.available.names[0]
  subnet_id         = data.aws_subnet.ec2_subnet.id
  tags = {
    "Name" = "TF-Lab-Server"
  }
}

resource "aws_ebs_volume" "ebs_volumes" {
  count             = var.ec2_instance_count * var.ebs_vol_count
  availability_zone = element(aws_instance.ec2_instances.*.availability_zone, floor(count.index / var.ebs_vol_count))
  size              = var.ebs_volume_sizes[count.index % var.ebs_vol_count]
}

resource "aws_volume_attachment" "ebs_vol_attach" {
  count       = var.ec2_instance_count * var.ebs_vol_count
  volume_id   = aws_ebs_volume.ebs_volumes.*.id[count.index]
  device_name = var.ec2_device_names[count.index % var.ebs_vol_count]
  instance_id = element(aws_instance.ec2_instances.*.id, floor(count.index / var.ebs_vol_count))
}
