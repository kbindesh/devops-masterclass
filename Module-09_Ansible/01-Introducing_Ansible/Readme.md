# Introduction to Ansible

- Ansible is an open source community project sponsored by Red Hat | Developed by <b>Michael DeHaan</b>
- Ansible is a powerful tool which can be used for automating IT tasks (e.g. software installation, configuring servers, deploying apps etc)
- Ansible is _agentless_, relying on temporary remote connections via SSH/WinRM
- Red Hat acquired Ansible in October 2015
- [Ansible GitHub repository](github.com/ansible/ansible.git)
- [Ansible Official Website](www.ansible.com)
- Code for Ansible is written in YAML (http://yaml.org/), which stands for _YAML Ain't Markup Language_.

## What can you automate with Ansible ?

- Hybrid cloud automation
- Network Automation
- IT Infrastructure provisioning
- Configuration Management
- Security Automation
- Edge Automation

## Performing IT management With and Without Ansible

### 1. Without Ansible

<img src="https://github.com/novatecstack/ansible-masterclass/assets/121426292/9fe1f16e-5ceb-4b60-ac7f-205b89e3bf33" data-canonical-src="https://github.com/novatecstack/ansible-masterclass/assets/121426292/9fe1f16e-5ceb-4b60-ac7f-205b89e3bf33" width="600" height="220" />

### 2. With Ansible

<img src="https://github.com/novatecstack/ansible-masterclass/assets/121426292/00dd9d91-8fcd-410c-a369-e946cebadd77" data-canonical-src="https://github.com/novatecstack/ansible-masterclass/assets/121426292/00dd9d91-8fcd-410c-a369-e946cebadd77" width="600" height="270" />

## How does Ansible work ?

The Ansible is agentless; in order to perform certain tasks on Servers (physical or virtual), it connects over the SSH and then executes playbook instructions on target machines.

<img src="https://github.com/novatecstack/ansible-masterclass/assets/121426292/84a9e448-513b-42e4-b249-9a90af6fa135" data-canonical-src="https://github.com/novatecstack/ansible-masterclass/assets/121426292/84a9e448-513b-42e4-b249-9a90af6fa135" width="600" height="290" />

## What do I need to know for learning Ansible?

- Connect to a remote machine using SSH
- Interact with the Bash command-line shell (pipes and redirection)
- Install packages
- Use the sudo command
- Check and set file permissions
- Start and stop services
- Set environment variables
- Write scripts (any language)

## [Ansible: Releases and maintenance](https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html)

Ansible's community packages are distributed in two ways:

- **ansible-core**: a minimalist language and runtime package containing a set of _Ansible.Builtin_.
- **ansible**: a much larger batteries included package, which adds a community-curated selection of Ansible collections for automating a wide variety of devices.

## Ansible CLI Tools

- ansible
- ansible-playbook
- ansible-doc
- ansible-inventory
- ansible-galaxy
- ansible-console
- ansible-test
- ansible-connection
- ansible-pull
- ansible-vault
