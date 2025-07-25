# `Docker` Practice Questions

You may try to answer the following questions to assess your learning progress:

## Docker Fundamentals

- Which statements are correct (multiple answers are possible)?

  - A container is kind of a lightweight VM
  - A container only runs on a Linux host
  - A container can only run one process
  - The main process in a container always has PID 1
  - A container is one or more processes encapsulated by Linux namespaces and restricted by cgroups

- In your own words, using analogies, explain what a container is.
- Why are containers considered to be a game-changer in IT? Name three or four reasons.
- What does it mean when we claim, if a container runs on a given platform, then it runs anywhere? Name two to three reasons why this is true.

- How much does a typical enterprise save when containerizing its legacy applications?
  - 20%
  - 33%
  - **50%** or more
  - 75%

7. Which two core concepts of Linux are containers based on?
8. On which operating systems is Docker Desktop available?

# Container Lifecycle

- Which two important concepts of Linux are enabling factors -r containers?
- What are the possible states a container can be in?
- Which command helps us to find out which containers are currently running on our Docker host? | And list all the containers.
- Which command is used to list only the IDs of all containers?

## Docker Images

- How would you create a Dockerfile that inherits from Ubuntu version 22.04, and that installs ping and runs ping when a container starts? The default address used to ping should
  be 127.0.0.1.
- How would you create a new container image that uses alpine:latest as a base image and installs curl on top of it? Name the new image my-alpine:1.0.
- Create a Dockerfile that uses multiple steps to create an image of a Hello World app of minimal size, written in C or Go.
- Name three essential characteristics of a Docker container image.
- You want to push an image named foo:1.0 to your _kbindesh_ personal account on Docker Hub. Which of the following is the right solution?
  - $ docker container push foo:1.0
  - $ docker image tag foo:1.0 kbindesh/foo:1.0
  - $ docker image push kbindesh/foo:1.0
  - $ docker login -u kbindesh -p <your password>
  - $ docker image tag foo:1.0 kbindesh/foo:1.0
  - $ docker image push kbindesh/foo:1.0
  - $ docker login -u kbindesh -p <your password>
  - $ docker container tag foo:1.0 kbindesh/foo:1.0
  - $ docker container push kbindesh/foo:1.0
  - $ docker login -u kbindesh -p <your password>
  - $ docker image push foo:1.0 kbindesh/foo:1.0

## Docker Volumes

- How would you create a named data volume with a name such as _my-products_ using the default driver?
- How would you run a container using the Alpine image and mount the my-products volume in read-only mode into the /data container folder?
- How would you locate the folder that is associated with the my-products volume and navigate to it? Also, how would you create a file, sample.txt, with some content?
- How would you run another Alpine container where you mount the my-products volume to the /app-data folder, in read/write mode? Inside this container, navigate to the /app-data
  folder and create a hello.txt file with some content.
- How would you mount a host volume – for example, ~/my-project – into a container?
- How would you remove all unused volumes from your system?
- The list of environment variables that an application running in a container sees is the same
  as if the application were to run directly on the host.
  - True
  - False

## Docker Compose

- What is Docker Compose, and what is it used for?
- What is a Docker Compose file, and what are some of the key elements it can contain?
- How can you use Docker Compose to start and stop an application, and what are some of the key command-line options?
- What are some of the benefits of using Docker Compose to manage multi-container applications?
- How do you use docker-compose to run an application in daemon mode?
- How do you use docker-compose to display the details of the running service?
- How do you scale up a particular web service to, say, three instances?
