# Docker Images and Registry

## Docker Image

- A **Docker image** is a read-only template that contains a set of instructions for creating a container that can run on the Docker platform
- It provides a convenient way to package up applications and preconfigured server environments, which you can use for your own private use or share publicly with other Docker users
- A Docker image is made up of a collection of files that bundle together all the essentials – such as installations, application code, and dependencies – required to configure a fully operational container environment

<img src="" width="550" height="400" class="center">

## Docker Containers

## `Containers` vs `Virtual Machines`

## Application Deployment with Docker

### Step-01: Pulling the Docker Image from Registry

### Step-02: Running Containers

### Step-03: Config Port Mapping

## Docker Registry - `Docker Hub`

### Step-01: Create Docker Account

### Step-02: Develop the Application code

- You may download the application code from [app-code](app-code)

### Step-03: Build the Container Image

```
docker build ./app-code -t bin-web-app

```

### Step-04: Verify the Image

```
docker images

```

### Step-05: Run the container locally

```
docker run -d -p 8080:80 aci-tutorial-app

```

### Step-06: Access the Application

- Now, navigate to http://vm_ip_or_dns_name_here:8080 in your browser to confirm that the container is running.
- You should see a web page similar to the following:
