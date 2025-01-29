# Understanding Single-Host Networking

## Container Network Model (CNM)

- So far, we have seen single container applications, but in a real environment, a containerized business application consists of several containers that need to collaborate to achieve a goal.
- So, we need a way for an individual containers to communicate with each other.
- You can achieve it with the help of _Networks_, which we can be used to send data packets back and forth between containers.
- Docker has a simple networking model, called **Container Network Model (CNM)**, to specify the network requirements of any application.

[Docker CNM HERE]()

## CNM Elements

1. Network Sanboxes
2. Endpoints
3. Network

## Docker Network types

1. **Bridge**

   - **Scope**: Local
   - Simple network based on Linux bridges to allow networking on a single host.

2. **Macvlan**

   - **Scope**: Local
   - Configures multiple layer-2 addresses (MAC) on a single physical host interface

3. **Overlay**

   - **Scope**: Global
   - Multi-node capable container network based on Virtual Extensible LAN (VXLan)

## Docker Network Commands

```
# List all the Docker Networks present on a Host
docker network ls

# In order to get more details about a network, use inspect
docker network inspect bridge

# Create a new bridge network, say "webapp-network"
$ docker network create --driver bridge webapp-network

# Run a container in the above created network, say "webapp-network"
docker container run --name webapp1 -d --network webapp-network nginx:alpine

# Run another container in the same network as "webapp1" container
docker container run -it --rm --webapp2 container:webapp1 alpine:latest /bin/sh

# --network container:webapp2 means that the webapp2 container will use the same network namespace as the container called webapp1.

```
