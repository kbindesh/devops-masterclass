# Creating and Managing Docker Containers

## What are Docker Images?

- A **Docker image** is a read-only template that contains a set of instructions for creating a container that can run on the Docker platform
- It provides a convenient way to package up applications and preconfigured server environments, which you can use for your own private use or share publicly with other Docker users
- A Docker image is made up of a collection of files that bundle together all the essentials – such as installations, application code, and dependencies – required to configure a fully operational container environment

### The layered filesystem

- Container images are templates from which containers are created. These images are not made up of just one monolithic block but are composed of many layers.
- The first layer in the image is also called the **base layer**.
- Each layer contains some files and folders.
- Each layer only contains the changes to the filesystem concerning the underlying layers.
- The **layers of a container image are all immutable**. Hence, once generated, the layer cannot ever be changed.

## What is `Docker Registry (Docker Hub)` ?

## Hands-on Labs

### Step-00: Prerequisites

- [Docker Client & Server](../02_Docker_Installation/Readme.md)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [Git](https://git-scm.com/downloads)

### Step-01: Create a new Dockerhub account

- For creating a new Dockerhub Account, navigate to https://hub.docker.com/signup and follow the process.

### Step-02: Develop the Application code

- You may download the application code from [app-code](app-code/app-code.zip) on your Docker host or clone this [repository >>](https://github.com/kbindesh/docker-image-lab-repo)

```
# Create a new directory for storing all the app code + Dockerfile
mkdir docker-img-lab

# Move the control to above created directory
cd docker-img-lab

# Clone the application code on Docker host
git clone https://github.com/kbindesh/docker-image-lab-repo.git

# Get inside the cloned repo directory
cd docker-image-lab-repo
```

### Step-03: Build the Container Image

```
# Build a new docker image and tag it with some name
docker build ./app-code -t bin-web-app

```

### Step-04: Verify the Image

```
docker images

```

### Step-05: Run the container locally

```
# Create and start the container using custom image created in step#3
docker run -d -p 8080:80 bin-web-app

```

### Step-06: Access the Application

- Now, navigate to http://vm_ip_or_dns_name_here:8080 in your browser to confirm that the container is running.
- You should see a web page similar to the following:

### Step-07: Push the Docker Image to Docker Registry (DockerHub)

- Pre-requisite: A Docker Hub Account | You may create it from here: https://hub.docker.com/signup

```
# Sign-in to Docker Hub
docker login

# Tag docker image as per Docker Hub naming convention
docker build -t docker_acc_username/image-name:tag .

docker build -t kbindesh/dockerwebapp:v1 .

# Push the image to Docker Hub
docker push complete_img_name:tag

docker push kbindesh/dockerwebapp:v1

```

### Step-08: Push the Docker Image to AWS Elastic Container Registry (ECR)

- [Install AWS CLI on Dockerhost]()
- **Connect to your AWS Account using AWS CLI**

```
# Sign-in to AWS Account
aws configure

```

- **Create an AWS ECR Repo**

```
# Syntax
aws ecr create-repository --repository-name <repo_name> --region <region_name>

# Example
aws ecr create-repository --repository-name bin-ecr-repo --region us-east-1

# Reference
https://docs.aws.amazon.com/cli/latest/reference/ecr/create-repository.html
```

- **Login to AWS Elastic Container Registry (ECR)**

```
aws ecr get-login-password --region <region_name>

# Connect to ECR using the token generated in the previous step
aws ecr --region <region> | docker login -u AWS -p <encrypted_token> <ecr_repo_uri>

# Reference
https://docs.aws.amazon.com/cli/latest/reference/ecr/get-login-password.html
```

- **Tag your image as per ECR Image naming convention**

```
docker tag <source_image> <target_ecr_repo_uri>

```

- **Push the Docker Image to ECR**

```
docker push <container_image_img>:<tag>
```
