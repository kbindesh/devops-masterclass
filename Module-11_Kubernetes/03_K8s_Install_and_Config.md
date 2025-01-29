# Install and configure Kubernetes

- In this module, we will setup a kubernetes cluster.
- There are various kubernetes distributions available out of which here we'll setup below two distros:
  - **minikube** - single node k8s (for learning)
  - **kubeadm** - multi-node k8s (prod grade)
  - **Amazon EKS** - multi-node k8s (prod grade)
  - Microsoft AKS - multi-node k8s (prod grade)
  - GKE - multi-node k8s (prod grade)
  - Rancher K8s
  - K3s
  - MicroK8s

## 1. Install and Configure `minikube` kubernetes

- _minikube_ is local Kubernetes, focusing on making it easy to learn and develop for Kubernetes.

### Step-00: Prerequisites

- 2 CPUs or more
- 2GB of free memory
- 20GB of free disk space
- Internet connection
- Container or virtual machine manager, such as: Docker, QEMU, Hyperkit, Hyper-V, KVM, Parallels, Podman, VirtualBox, or VMware Fusion/Workstation

### Step-01: Provision an EC2 Instance (for this lab)

- **AMI**: Amazon Linux 2
- **Instance Type**: t2.medium (atleast 2 CPU and 2 GB memory)
- **SG Ingress**: Allow SSH (22)
- **SG Egress**: Allow all
- **VPC**: Default
- **Subnet**: Default
  Note: This configuration will not be considered under free tier usage and you may get billed for it. Therefore, kindly make sure to shutdown the server instance, whenever not in use.
- **Public IP**: Enable

- :warning: **Note**: This configuration will not be considered under free tier usage and you may get billed for it. Therefore, kindly make sure to shutdown the server instance, whenever not in use.

### Step-02: Install Docker

- **Install using EC2 User data script**

  - You may refer to this [EC2 user-data script](./ec2-minikube-install-script/amzon-lnx2-minikube-install.sh) for setting up minikube k8s cluster on EC2 instance while provisioning it (add this script in the user-data section of your EC2 instance).
  - **Note**: In case you are setting up k8s env using this method, skip **step#3, step#4** and **step#5**

- **Install by manually running commands**

```
# Install Docker on Amazon Linux 2 AMI
sudo amazon-linux-extras install -y docker

# Start the docker service
sudo systemctl start docker

# Enable the docker service
sudo systemctl enable docker

# Add the ec2-user to docker group
sudo gpasswd -a ec2-user docker

```

### Step-03: Install `kubectl` command line utility

- **kubectl** is a utility to manage a K8s cluster.
- It is required to install it before you configure or install the K8s cluster.

```
# Download the kubectl binary
sudo curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

# Provide execute permission to kubectl
sudo chmod +x kubectl

# Move the kubectl program to /usr/local/bin in order to access it from anywhere
sudo mv kubectl /usr/local/bin

```

### Step-04: Install `minikube`

- Once both Docker and Kubectl are installed, you may use following set of commands to install Minikube:

```
 # Download the minikube binary
 sudo curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64

 # Install the minikube in /usr/local/bin/ directory
 sudo install minikube-linux-amd64 /usr/local/bin/minikube

 # Restart the VM
 shutdown -r now

```

### Step-05: Start the `minikube` k8s cluster

```
# Start the minikube cluster
 minikube start

# Finally, you may check the status of the installation
minikube status

```

## 2. Install and Configure `kubeadmin` k8s cluster

## 3. Install and Configure `Amazon EKS` cluster

## References

- [Minikube Official Documentation](https://minikube.sigs.k8s.io/docs/)
- [Install and Set Up kubectl on Linux](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)
- [Install Docker Engine](https://docs.docker.com/engine/install/)
