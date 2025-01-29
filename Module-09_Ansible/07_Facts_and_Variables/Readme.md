# Ansible Variables

## What are Variables in ansible?

- Variables stores information that varies with each host or a group of hosts.
- Ansible variables are dynamic values used within Ansible playbooks and roles to enable customization, flexibility, and reusability of configurations.

## Why are variables useful in Ansible?

- The use of variables simplifies the management of dynamic values throughout an Ansible project and can potentially reduce the number of human errors.
- We have a convenient way to handle variations and differences between different environments and systems with variables.
- We have the flexibility to define them in multiple places with different precedence according to our use case.
- We can also register new variables in our playbooks by using the returned value of a task.

## Variable naming convention

- Variable names can contain only letters, numbers, and underscores and must start with a letter or underscore.
- Some strings are reserved for other purposes and aren't valid variable names, such as [Python Keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords) or [Playbook Keywords](https://docs.ansible.com/ansible/latest/reference_appendices/playbooks_keywords.html#playbook-keywords).
- The variable names should be short and meaningful, because otherwise, you will have a hard time while debugging the issues.

- **Good Variable Names**
  - ssh_private_key
  - web_server_port
  - max_retries
  - key_pair_path

## Type of Variables in Ansible (based on datatype)

- **String Variables**

```
greeting: "Hello world"
username: "dbuser"
```

- **Number Variables**

```
no_of_retries:5
max_api_connections: 10
```

- **Boolean Variables**

```
# Valid values for True are: True, 'true', 'yes', 'y', 'on'
become_admin: true

# Valid values for False are: False, 'false', 'no', 'n', 'off'
debug_mode: false
```

- **List Variables**

```
vars:
  variable_name:
    - docker
    - git
    - httpd
```

- **Dictionary Variables**

```
# Syntax
variable:
  key1: value1
  key2: value2
  key3: value3

# Example: Dictionary variable
- name: Print Dictionary Variables lab
  hosts: all
  vars:
    user:
      username: "binusr"
      project: "project1"
  tasks:
    name: Print username and project details
    ansible.builtin.debug:
      msg: "Username is {{ user.username }} and Project is {{ user.project }}"
```

- **Register Variables**
  - You can create variables from the output of an Ansible task with the task keyword register.
  - You can use registered variables in any later tasks in your play.

```
- name: Register variable demo
  hosts: webservers
  tasks:
    - name: Get the hosts details
      ansible.builtin.shell: cat /etc/hosts
      register: hosts_details

    - name: Display host details
      ansible.builtin.debug:
        var: host_details
```

## Type of Variables in Ansible (based on its definition)

Variables in Ansible can come from different sources and can be used in playbooks, roles, inventory files, and even within modules.

- **Group variables** – Similar to host variables but used for a group of hosts and are defined in the inventory or separate files in the group_vars directory.

```
# This is an Inventory/Host file

# Host variables
webserver1 ansible_hosts=192.168.10.15 gateway_ip=192.168.10.2
webserver2 ansible_hosts=192.168.10.18 gateway_ip=192.168.10.2

[webservers]
webserver1
webserver2

# Group variables
[webservers:vars]
gateway_ip=192.168.10.1

# Variable defined at the host level get the precedence over the group level variables
```

- **Inventory variables** – These variables are defined in the inventory file itself and can be applied at different levels (host, group, all groups).

```
# This is an Inventory/Host file - /etc/ansible/hosts

webserver1 ansible_hosts=192.168.10.15 gateway_ip=192.168.10.2
webserver2 ansible_hosts=192.168.10.18 gateway_ip=192.168.10.2

[webservers]
webserver1
webserver2

[webservers:vars]
gateway_ip=192.168.10.1

# Variable defined at the host level get the precedence over the group level variables
```

- **Playbook variables** – These variables are used to pass values into playbooks and roles and can be defined inline in playbooks or included in external files.

```
---
- name: Configure Gateway Server
  hosts: webservers
  vars:
    gateway_ip: 192.168.10.3
  tasks:
    ansible.builtin.debug:
      msg: "{{ gateway_ip }}"

# Variable defined at the playbook level get the precedence over the inventory variables (hosts/group)
```

- **Extra variables** – Passed to Ansible at runtime using the **-e** or **–extra-vars** command-line option. They have the highest precedence and can be used to override other variables or to pass data that might change between executions.

```
ansible-playbook playbook_name.yml --extra-vars "subnet_cidr=10.20.0.0/16"
```

- **Task variables** – These variables are specific to individual tasks within a playbook. These can override other variable types for the scope of the task in which they are defined.
- **Host variables** – Specific to hosts, these variables are defined in the inventory or loaded from external files or scripts and can be used to set attributes that differ between hosts.
- **Fact variables** – Gathered by Ansible from the target machines, facts are a rich set of variables - (including IP addresses, operating system, disk space, etc.) that represent the current state of the system and are automatically discovered by Ansible.
- **Role variables** – Defined within a role, these variables are usually part of the role’s default variables (defaults/main.yaml file) or variables intended to be set by the role user (vars/main.yaml file) and are used to enable reusable and configurable roles.
- **Magic variables** – Special variables such as hostvars, group_names, groups, inventory_hostname, and ansible_playbook_python, provide information about the execution context and allow access to inventory data programmatically.

```
# Syntax
msg: "{{ hostvars['host_alias'].variable_name}}"

# Example
msg: "{{ hostvars['webserver'].ansible_host }}"
msg: "{{ hostvars['webserver'].ansible_facts }}"
msg: "{{ hostvars['webserver'].ansible_facts.architecture }}"
```

- **Environment variables** – Used within Ansible playbooks to access environment variables from the system running the playbook or from remote systems.

### Playbook Variables

- **String variable**

```
---
- name: Variable Demo
  hosts: all
  become: yes
  become_user: root
  vars:
    username: bindesh
  tasks:
  - name: Add the user {{ username }}
    ansible.builtin.user:
      name: "{{ username }}"
      state: present
```

- **List Variable**

```
---
- name: List variables demo
  hosts: all
  become: true
  become_user: root
  vars:
    cidr_blocks:
        production:
          vpc_cidr: "172.31.0.0/16"
        staging:
          vpc_cidr: "10.0.0.0/24"
  tasks:
  - name: Print Production CIDR
    ansible.builtin.debug:
      var:
        cidr_blocks['production']['vpc_cidr']

  - name: Print staging CIDR
    ansible.builtin.debug:
      var:
        cidr_blocks['staging']['vpc_cidr']

```

### Special variables

- Ansible special variables are a set of predefined variables that contain information about the system data, inventory, or execution context inside an Ansible playbook or role.
- The names of these variables are reserved.

### Magic variables

- Magic variables are automatically created by Ansible and cannot be changed by a user.
- These variables will always reflect the internal state of Ansible, so they can be used only as they are.
- For more details, refer https://docs.ansible.com/ansible/latest/reference_appendices/special_variables.html#magic-variables

```
---
- name: Echo playbook
  hosts: localhost
  gather_facts: no
  tasks:
    - name: Echo Inventory_hostname
      ansible.builtin.debug:
        msg:
          - "Hello from Ansible playbook!"
          - "This is running on {{ inventory_hostname }}"

```

## References

- [Ansible Variables](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#)
-
