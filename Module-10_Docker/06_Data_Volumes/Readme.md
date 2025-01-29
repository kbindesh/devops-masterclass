# Data Volumes and Configurations

## Creating and mounting data volumes

### Step-00: Modifying the container layer

```
# Run a container and Create a new file inside it
docker container run --name demo alpine /bin/sh -c 'echo "test message" > test.txt'

# Use the diff command to find out what has changed in the container's filesystem as compared to original image
docker container diff <container_name>

docker container diff demo
```

- Now, if the container is deleted from memory, its container layer will also be removed, and with it, all the changes will be irreversibly deleted.
- If we need our changes to persist even beyond the lifetime of the container, **Docker volumes** are the solution.

### Step-01: Create a Volume | List | Inspect

```
docker volume create <volume_name>

docker volume create datavolume
```

- The default volume driver is the so-called **local driver**, which stores the data locally in the host filesystem.

- **List all the Volumes known to Docker**

```
docker volume ls

# Reference
https://docs.docker.com/reference/cli/docker/volume/ls/
```

- **Get more details about a particular Docker Volume**

```
docker volume inspect <volume_name>

docker volume inspect datavolume
```

### Step-02: Mounting a volume on Container

- Once we have created a named volume, we can mount it into a container by following these steps:

```
# Use the --volume or -v parameter with docker container run command
docker container run -it --name <container_name> -v <vol_name>:/<dir> alpine /bin/sh

docker container run -it --name container2 -v datavolume:/data alpine /bin/sh

# Inside the container, we can now create files in the /data folder
/ # cd /data
/ # echo "Some app code" > Code-01.txt
/ # echo "Some more code" > Code-02.txt

# Exit from the Container
Press Ctrl+D
```

### Step-03: Delete the Container with Volume mounted on it

```
# Delete the container we created in the previous step
docker container rm container2
```

### Step-04: Create a new Container and mount the Volume created in Step#1 on it

```
docker container run --name container4 -it --rm \
-v datavolume:/app/data \
centos:7 /bin/bash
```

- Once you're inside the CentOS container, we can navigate to the `/app/data` folder to which we have mounted the volume and list its content:

```
cd /app/data
ls –l

# As expected, we should see the two files create in step#2
Code-01.txt
Code-02.txt

# Exit from the Container
Press Ctrl+D
```

### Step-05: Removing volumes

```
# To remove/delete one volume
docker volume rm <volume_name>

# To check the list of all the remaining Data volumes
docker volume ls

# To remove all the containers to clean up
docker container rm -v -f $(docker container ls -aq)
```

### Step-06: `Sharing Data` between containers `using Docker Volumes`

- Containers are like sandboxes for the applications running inside them.
- This is really helpful to protect applications running in different containers from conflicting with each other.
- It means that the whole filesystem visible to an application running inside a container is private to that application, and no other application running in a different container can interfere with it.
- **Sample Use-case**:
  - We want to share data between containers.
  - Say an application running in **container-A** produces some data that will be consumed by another application running in **container-B**.
  - In order to make it work, we can create a volume and mount it to _container-A_, as well as to _container-B_.

```
# Create a container and mount a volume on it | Default volume mode: R/W
docker container run -it --name ContainerWithRWVolume -v shared-data:/data .alpine /bin/sh

# Create a new file inside the container (on mounted volume)
/ echo "New file present in docker volume" > /data/test-file.txt

# Now, exit from the container by pressing Ctrl+D or exit

# Create another container, say ContainerWithROVolume and mount a volume in Read Only mode
docker container run -it --name ContainerWithROVolume -v shared-data:/app/data:ro ubuntu:22.04 /bin/bash

# Check in the container if you can see the file created in the ContainerWithRWVolume container
ls -l /app/data

# Now, try to create a new file on the mounted volume
/ echo "New file for read only volume" > /app/data/test-file-2.txt

# It will fail with the following message:
bash: /app/data/test-file-2.txt: Read-only file system
```

- Exit from the container and remove all the containers and volumes once done with the lab.

```
docker container rm -f $(docker container ls -aq)

docker volume rm $(docker volume ls -q)

# Docker CLI References for above commands
# https://docs.docker.com/reference/cli/docker/container/ls/
# https://docs.docker.com/reference/cli/docker/container/rm/
# https://docs.docker.com/reference/cli/docker/volume/ls/
# https://docs.docker.com/reference/cli/docker/volume/rm/

```

### Step-07: Using Host volumes

### Step-08: Defining Volumes in Docker Image
