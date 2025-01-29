# 2. Docker Installation

<img src="images/dockerlogo.png" width="300" height="160" />

## Docker Installation - `Docker Desktop` & `Docker Engine`

### 01. Docker Desktop Installation | Supports Linux, Windows & MacOS

- **Docker Desktop** is a one-click-install application for your Mac, Linux, or Windows environment that lets you build, share, and run containerized applications and microservices.
- It provides a GUI (Graphical User Interface) that lets you manage your containers, applications, and images directly from your machine.
- Docker Desktop includes following components:
  - Docker Engine
  - Docker CLI client
  - Docker Scout
  - Docker Build
  - Docker Extensions
  - Docker Compose
  - Docker Content Trust
  - Kubernetes
  - Credential Helper
- [Docker Desktop Installation](https://docs.docker.com/desktop/)

### 02. Docker Engine Installation | Supports Linux machines only

#### Step-01: Provision a VM (for this lab an EC2 Instance with Amazon Linux 2 AMI), say `Dockerhost`

#### Step-02: Connect to the Dockerhost machine (SSH)

#### Step-03: Install Docker on Linux Systems

- You may refer to this link for Docker engine installation guide: https://docs.docker.com/engine/install/
- (Optional) Or you may pass [ec2 user data script](scripts/amzn-linux-2-docker-install.sh) while performing Step-01.

#### Step-04: Check Docker Version & Start the Docker Daemon

```
# Check the current installed version of Docker
docker version

# Start the Docker service
sudo systemctl start docker

```

#### Step-05: Config Dockerhost for current user

```
# Add ec2-user to docker group
usermod -a -G docker ec2-user

```

#### Step-06: Display Docker Engine details | Containers, Plugins, Images etc.

```
docker info

```

## Docker Configurations

### List all Docker commands

```
docker
```

### Docker commands help

```
docker <command> --help
```

## Docker: Reference Links

- [Docker Overiew](https://docs.docker.com/get-started/overview/)
- [Docker Desktop](https://docs.docker.com/desktop/)
- [Docker Engine](https://docs.docker.com/engine/)
- [Install Docker Engine](https://docs.docker.com/engine/install/)
- [Docker Images and Build](https://docs.docker.com/build/)
- [Docker Storage](https://docs.docker.com/storage/)
- [Docker Networking](https://docs.docker.com/network/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Docker Swarm](https://docs.docker.com/get-started/orchestration/)
