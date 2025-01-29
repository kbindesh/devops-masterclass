# Configuring Containers

- The configuration is often used to allow the same container to run in very different environments, such as in development, test, staging, or production environments.
- In Linux, config values are usually provided via environment variables.
- Important thing to consider is _the environment variables that we see on the host are different from the ones that we see within a container_.
- Let's try to understand it with the help of an example:

```
# Display a list of all environment variables
export

# Now, let's run a shell inside an Alpine container
docker container run --rm -it alpine /bin/sh

# After getting inside of the container, check it's env variables
/ # export

# Press Ctrl+D or exit to leave from container and stop it

```

## Step-01: Defining `environment variables` using parameter (--env or -e)

- We can pass some configuration values into the container in the form environment variables while creating it.
- Use **--env** or **-e** parameter

```
# Syntax
docker container run --rm -it --env <key>=<value> alpine /bin/sh

# Example-01
docker container run --rm -it --env LOG_DIR=/var/log/dev-logs \
alpine /bin/sh

# Example-02
docker container run --rm -it --env LOG_DIR=/var/log/prod-logs \
alpine /bin/sh

```

- **To check the LOG_DIR environment variable value from within the container**

```
/ # export | grep LOG_DIR

```

- **You can define more than one environment variable while creating a container**.

```
# Defining 3 env variables while creating a container
docker container run --rm -it --env LOG_DIR=/var/log/dev-logs \
--env MAX_LOG_FILES=2 --env MAX_LOG_SIZE=2G alpine /bin/sh

# to check the values of all the env variables
/ # export
```

## Step-02: Defining `environment variables` using config files (--env-file)

```
# Create a file called production.config, and below env variables to it
LOG_DIR=/var/log/prod-logs
MAX_LOG_FILES=2
MAX_LOG_SIZE=2G

# Now create a container by passing the above file as env file
docker container run --rm -it \
--env-file ./production.config alpine sh -c "export | grep LOG"
```
