amazon-linux-extras install -y epel
amazon-linux-extras disable ansible2
yum-config-manager --enable epel
yum --enablerepo epel install -y ansible
ansible --version