# Terraform Questions

## What is IaC (Infrastructure-as-Code)?

## What are the various Terraform commands? Terraform Workflow

Some of the most useful Terraform commands are:

- terraform init - initializes the current directory as a Terraform directory
- terraform refresh - refreshes the state file
- terraform output - views Terraform outputs
- terraform plan - a dry run to see what Terraform will do if the code is applied
- terraform apply - applies the Terraform code and create/modify/delete the real resources
- terraform destroy - destroys/deletes any existing resources created by Terraform
- terraform graph - creates a DOT-formatted graph

## What are various Terraform editions available?

- Self-hosted
- Cloud

## What are Terraform Providers? List few on which you have worked upon?

- AWS
- Azure
- GCP
- Random
- Kubernetes

## List various Terraform file formats.

- .tf
- .tfvars
- .tfstate
- .tfstate.backup
- .lock.hcl

## What are the various top-level blocks in Terraform and it's significance?

- terraform
- provider
- resource
- variable
- output
- local
- data (data source)
- modules

## Explain more about current state vs desired state in Terraform context.

## What is Terraform Registry?

## What is DRY principle in Terraform?

- Don't Repeat Yourself

## Terraform scripts are written in which language? And which file format can be used?

## Define _null_ resource in Terraform.

## What do you understand by _terraform backend_?

- A Terraform backend defines where Terraform stores its state file and how it manages concurrent operations like state locking.
- The state file is a crucial component of Terraform, as it maps the resources defined in your configuration to the real-world infrastructure provisioned in your cloud provider or on-premises environment.

## List few major competitors/alternative solutions of Terraform.

- Some of the top competitors and alternatives to Terraform are:
  - Pulumi
  - OpenTofu
  - CrossPlane
  - AWS CloudFormation
  - ARM Templates
  - CDK
  - Ansible

## What are modules in Terraform?

- Modules are collection of resources that are clubed into a logical grouping.
- The root module includes resources mentioned in the .tf files and is required for every Terraform.

## Can we use Terraform for an on-prem infrastructure?

- Yes, Terraform can be used for on-prem infrastructure. As there are a lot of obtainable providers, we can decide which suits us the best. All that we need is an API.

## Does Terraform support multi-provider deployments?

- Yes, multi-provider deployments are supported by Terraform, which includes on-prem systems like:
  - Openstack
  - VMware, and we can manage SDN even using Terram.

## How is duplicate resource error ignored during terraform apply?

You may go for the following options:

- Delete those resources from the cloud provider(API) and recreate them using Terraform
- Delete those resources from Terraform code to stop its management with it
- Carry out a terraform import of the resource and remove the code that is trying to recreate them

## What are provisioner in Terraform? List some of the built-in provisioners available in Terraform.

Here is the list of built-in provisioners in Terraform:

- Salt-masterless Provisioner
- Remote-exec Provisioner
- Puppet Provisioner
- Local-exec Provisioner
- Habitat Provisioner
- File Provisioner
- Chef Provisioner

## What is _Terraform graphs_ ?

The Terraform graph command generates a visual representation of the dependency relationships between resources in your Terraform configuration or execution plan, helping you to understand the structure and dependencies within your infrastructure.

```
# To generate a Terraform graph type

terraform graph [options]

# Terraform graph examples

terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.23.1"
    }
  }
}

provider "docker" {
  host = "tcp://localhost:2375"
  #host = "unix:///var/run/docker.sock" # Docker on ubuntu connection
}

# Creating a Docker Image ubuntu with the latest as the Tag.
resource "docker_image" "ubuntu" {
  name = "ubuntu:latest"
}

# Creating a Docker Container using the latest ubuntu image.
resource "docker_container" "webserver" {
  image             = docker_image.ubuntu.latest
  name              = "terraform-docker-test"
  must_run          = true
  publish_all_ports = true
  command = [
    "tail",
    "-f",
    "/dev/null"
  ]
}

resource "docker_image" "nginx" {
  name         = "nginx:latest"
  keep_locally = false
}

resource "docker_container" "nginx" {
  image = docker_image.nginx.latest
  name  = "nginx-test"
  ports {
    internal = 80
    external = 8000
  }
}

resource "docker_network" "private_network" {
  name = "my_network"
}

resource "docker_volume" "shared_volume" {
  name = "shared_volume"
}
```

- To visualize the dependencies, you can simply run:

```
terraform graph
```

## How will you setup remote backend for Terraform code?

## How does Terraform manage remote state? | What are .tfstate files? | What are the recommended practices for storing .tfstate files and lock state info?

By default, Terraform stores the state locally, but for collaboration, it supports remote backends (S3 with DynamoDB for AWS, GCS for Google Cloud, or Terraform Cloud). Remote state enables:

- Shared access for multiple team members.
- State locking to prevent conflicts.
- Better security with encryption and controlled access.

## How does Terraform handle importing existing infrastructure, and what are the limitations?

- Terraform can import existing resources into its state using the terraform import command.
- However, it doesn’t automatically generate configuration files (the .tf files) for those resources, so you'll need to write them manually.

- There are some limitations to this import functionality:

  - Complex setups require manual configuration reconciliation.
  - Some resource types are not supported for import.
  - There is a drift risk if the imported resource configuration doesn’t match actual infrastructure.
