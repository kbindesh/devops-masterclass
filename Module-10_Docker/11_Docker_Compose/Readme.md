# Managing Containers with `Docker Compose`

- **Docker Compose** is a tool provider by Docker that makes it possible for you to run multi-container Docker applications defined using the Compose file format.
- With a compose file, you can create and start all of the services defined in your configuration with a single command.

## Understanding `declarative` vs `imperative` orchestration of containers

- Docker Compose is a Docker tool that is primarily used when you need to run and orchestrate containers running on a single Docker host.
- Docker Compose is embedded in the normal Docker CLI.
- Docker Compose uses files formatted in **YAML** format.
- By default, Docker Compose expects these files to be called **docker-compose.yml**, however other names are possible.
- The content of a **docker-compose.yml** file is a declarative way of describing and running a containerized **application essentially consisting of more than single container**.

- **What do you mean by `Imperative` here**?

  - This is a way in which we can solve problems by specifying the exact procedure
    that has to be followed by the system.

- **What do you mean by `Declarative` here**?

  - This is a way in which we can solve problems without requiring the developer
    to specify an exact procedure to be followed in order to accomplish a task.
  - You simply tell docker engine about your desired state for an application, and docker will figure out how to achieve it.
  - However this approach is inefficient and practically not possible to mid or large application with 100s of containers.
  - With the _Docker Compose_ tool, we are given a way to define the application in a declarative way in a file that uses the YAML format.

## How Docker Compose works?

- Docker Compose relies on a YAML configuration file, usually named **compose.yaml** or **docker-compose.yml**.
- The **compose.yaml** file follows the rules provided by the Compose Specification in how to define multi-container applications.

### The Compose application model

- **Services**
  - Computing components of an application are defined as _services_.
  - A service is an abstract concept implemented on platforms by running the same container image, and configuration, one or more times.
- **Networks**
  - Services communicate with each other through networks.
  - A network is a platform capability abstraction to establish an IP route between containers within services connected together.
- **Volumes**
  - Services store and share persistent data into volumes
- **Configs**
  - You may have services that require configuration data that is dependent on the runtime or platform.
- **Secrets**
  - Secrets can be for storing sensitive data that should not be exposed without security considerations.
  - Secrets are made available to services as files mounted into their containers.

## Multi-service application with Docker Compose

- If you want to run a multi-service application, you can of course start all the
  participating containers with the well-known _docker container run_ command.

### Step-00: Install and Configure `Docker Compose`

- For more details, refer https://docs.docker.com/compose/install/linux/
  
#### Compose V1 Installation (earlier)

```
# Download the docker compose binary
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) \
-o /usr/local/bin/docker-compose

# Move the docker-compose to /usr/bin/docker-compose dir for accessing it from anywhere
mv /usr/local/bin/docker-compose /usr/bin/docker-compose

# Assign the execute permission to docker-compose file
chmod +x /usr/bin/docker-compose

# Check the docker compose version
docker-compose --version
```

:warning: **Note** that Compose standalone uses the **-compose** syntax instead of the current standard syntax **compose**.

#### Compose V2 Installation (latest)

```
# Download and Install the Compose CLI plugin
DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
mkdir -p $DOCKER_CONFIG/cli-plugins
curl -SL https://github.com/docker/compose/releases/download/v2.27.0/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose

# Apply executable permissions to the binary
sudo chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose
or
sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-compose

# Check Docker Compose (v2) version
docker compose version
```

### Step-01: Create and analyze a docker-compose.yml file

- Download and Install VS Code IDE (https://code.visualstudio.com/download)
- Install Required VS Code Plugins: [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
- Create a new file with a label docker-compose.yml and add below config to it:

```
version: "3.8"
services:
  db:
    image: postgres:alpine
    environment:
    - POSTGRES_USER=dockeruser
    - POSTGRES_PASSWORD=dockerpass
    - POSTGRES_DB=pets
    volumes:
    - pg-data:/var/lib/postgresql/data
    - ./db:/docker-entrypoint-initdb.d

  pgadmin:
    image: dpage/pgadmin4
    ports:
      - "5050:80"
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@acme.com
      PGADMIN_DEFAULT_PASSWORD: admin
    volumes:
      - pgadmin-data:/var/lib/pgadmin

volumes:
  pg-data:
  pgadmin-data:

```

### Step-02: Run the services with the Docker Compose

- Connect to your Dockerhost and run the below command to deploy an app

```
# Move to the directory where you have your docker-compose.yml file
docker-compose up
```

- To verify the deployment, navigate to <docker_host_ip>:5050 from your local system and you should see the postgreSQL GUI sign-in page.
- Enter the credential mentioned in the compose.yml file and complete the sign-in process.

### Step-03: `Remove` the services with Docker Compose

- Once you're done with the above lab, press Ctrl+C to exit from the application and run below command to remove all the resources created as a result of Step#2

```
docker-compose down -v

# Above command will delete both the containers, volumes and a network

```

## `Building images` with Docker Compose

- To demonstrate the image build process with Docker compose, we need an application (code). You may refer to the code from [here >>](./image-build-sample-app/)

```
docker-compose build

# Building an Image with different name compose file
docker-compose  -f <docker_compose_file_name.yml> build

```

## `Running an application` with Docker Compose

- Once we have built our images, we can start the application using Docker Compose.

```
# Run the application in the background
docker-compose up --detach

OR

docker-compose up -d

# Running an application with different name compose file
docker-compose  -f <docker_compose_file_name.yml> up
```

- **List all services that are part of the application**

```
docker-compose ps

# To stop and clean up all the application
docker-compose down
```

## `Scaling a Service` with Docker Compose

- Running more instances is also called scaling out.

```
# Scale our web service to three instances
docker-compose up --scale web=3
```

## View example Projects that use Docker

- https://github.com/docker/awesome-compose 
