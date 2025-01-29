# Setting-up environment for `Ansible`

In this lab, there will be two machines:

- **Ansible Server (Controller node)** - where we will execute all the playbooks.

  - I've used Amazon Linux 2 ec2 instance for the Ansible controller.

- **Target Machine (client/managed node)** - to which "_Ansible Server_" will send the instructions mentioned via playbook tasks and eventually will be executed here.

  - I've used RHEL8 ec2 instance here.
  - You may use any other linux/windows machine.

- :warning: Make sure there is a connectivity between both the machines over SSH/RDP.

- Provision both the machines in the same Amazon VPC.

## Step-01: Setup `Ansible controller` (on Amazon EC2 instance)

### 1.1: Provision an EC2 instance

- AMI: Amazon Linux 2 (5.10 Kernel)
- Instance Type: t2.micro
- Key Pair: Create a new key pair
- VPC & Subnet: Default
- Security group: Allow SSH(22) ingress | Outbound allow all
- Storage: 10 GB (root volume)

### 1.2: Preparing `Ansible Controller` node for installing Ansible

```
sudo su -

# Update the hostname
vi /etc/hostname

[Delete the existing hostname and add a new one - ansible-controller]
[Save the file and exit]

# Create a new user for Ansible
useradd ansibleadmin
passwd ansibleadmin


# Add ansibleadmin user to the sudoers group
vi /etc/sudoers         # OR visudo
[shift+G]
ansibleadmin	ALL=(ALL)	NOPASSWD:ALL

# Now, sign-in as ansibleadmin user
sudo su - ansibleadmin

# Generate SSH keys for managed nodes (client)
ssh-keygen
[will create ssh keys under /home/ansibleadmin/.ssh directory]

exit
[logout from the ansibleadmin user | back to root user]

# Enable password based authentication
vi /etc/ssh/sshd_config
PasswordAuthentocation  yes

# Restart the sshd service
service sshd restart
```

### 1.3 Install and Configure `Ansible`

```
sudo su -

# Prerequisites | Check the following app versions to confirm
python --version
pip3 --version

# (Optional) Install Python if not already present
yum install -y python

# Install Ansible
pip3 install ansible

OR
yum install -y epel
amazon-linux-extras install -y ansible          # This command will work only in Amazon Linux 2

# Check the installed Ansible version
ansible --version

# Create a new directory of Ansible configurations - /etc/ansible
mkdir /etc/ansible
cd /etc/ansible

# Create a new file i.e. ansible.cfg in /etc/ansible/ directory
vi ansible.cfg
[You may download sample ansible.cfg from the below URI:]
[https://github.com/ansible/ansible/blob/stable-2.9/examples/ansible.cfg]

[save & exit]

# View the contents of the newly created ansible.cfg
more ansible.cfg

# Create a new file i.e. hosts in /etc/ansible/
touch hosts
[don't add any content to it yet]
```

## Step-02: Setup 'Managed Node 01' (on EC2 instance)

```
sudo su -

# Set the Hostname
vi /etc/hostname     - client
hostname client

# Create a new user for Ansible administration
useradd ansibleadmin
password ansibleadmin

[no need to generate a new keypair | will generate & copy from the ansible controller]

# Enable password based authentication
vi /etc/ssh/sshd_config
PasswordAuthentication yes

# Reload the sshd service
service sshd reload

# Add ansibleadmin user to the sudoers group
vi /etc/sudoers
OR
visudo

ansibleadmin	ALL=(ALL)	NOPASSWD:ALL
```

## Step-03: Establish connection between Ansible Controller & Managed Nodes

```
# Switch to controller node
sudo su -

vi /etc/ansible/hosts
[add private_ip in the file and save]

# Sign-in as ansible admin
sudo su - ansibleadmin

# Copy the ssh key to the managed node (client)
ssh-copy-id <private_ip _of_client_node>

[Enter the password of ansibleadmin user of controller node if prompted]
```

## Step-04: Test the Ansible setup

```
# Run ansible adhoc command to check the connectivity with the managed node
ansible all -m ping
```
