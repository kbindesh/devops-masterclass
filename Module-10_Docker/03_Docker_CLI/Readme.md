# Getting Started with Docker CLI (Client)

## How to use the Docker command line

- The base command for the Docker CLI is `docker`.
- For information about the available flags and subcommands, refer to the CLI reference.
- Depending on your Docker system configuration, you may be required to prefix each docker command with _sudo_.
- To avoid having to use sudo with the docker command, your system admin can create a Unix group called `docker` and add current logged-in user to it.

```
usermod -a -G docker ec2-user

```

## Docker Configuration Files

- By default, the Docker command line stores its configuration files in a directory called **.docker** within your **$HOME** directory.
- Docker manages most of the files in the _configuration_ directory and you shouldn't modify them.
- However, you can modify the **config.json** file to control certain aspects of how the docker command behaves.

## `Filter Commands` with Docker CLI

- The --filter flag expects a key-value pair separated by an operator.

```
# Syntax
docker COMMAND --filter "KEY=VALUE"

# Example
docker images --filter reference=alpine
```

- Combining filters: You can combine multiple filters by passing multiple --filter flags.

```
docker images --filter reference=alpine:latest --filter=reference=busybox

```

## Format command and log output
