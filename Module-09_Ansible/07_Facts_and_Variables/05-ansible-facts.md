# Ansible Facts

- I'm sure you must have already seen that when Ansible runs a playbook, before the first task runs, it says:

```
TASK [Gathering Facts]
*********************************************************
ok: [xxxxxx]
```

- When Ansible gathers facts, it connects to the hosts and queries it for all
  kinds of details about the hosts:

  - CPU architecture
  - Operating system
  - IP addresses
  - Memory info
  - Disk info, and more.

- You can access this data in the **ansible_facts** variable.

## Access Ansible facts using ad-hoc commands

- The setup module fetches all the details from the remote hosts to our controller nodes and dumps them directly to our screen (facts).

```
# Here, -m if for module
ansible all -m setup

#  Filtering out a specific value from Ansible facts
ansible all -m setup -a "filter=ansible_cmdline"
```

## Ansible Facts: Example-01

Let's see how we can use ansible_facts to gather operating system details of all the hosts:

```
---
- name: 'Ansible facts.'
  hosts: all
  gather_facts: true
  tasks:
    - name: Print out operating system details
      debug:
        msg: >-
          os_family:
          {{ ansible_facts.os_family }},
          distro:
          {{ ansible_facts.distribution }}
          {{ ansible_facts.distribution_version }},
          kernel:
          {{ ansible_facts.kernel }}
```

## Ansible Facts: Example-02

- Install Apache web server on RHEL and Ubuntu machines
- Remomeber, on RHEL systems, the Apache web server package is **httpd**, while in other distributions it's named **apache2**.

```
- hosts: all
  tasks:
  - package:
      name: "httpd"
      state: present
    when ansible_facts["os_name"] == "RedHat"
  - package:
      name: "apache2"
      state: present
    when ansible_facts["os_name"] == "Ubuntu"
```

## References

- https://www.redhat.com/sysadmin/playing-ansible-facts
