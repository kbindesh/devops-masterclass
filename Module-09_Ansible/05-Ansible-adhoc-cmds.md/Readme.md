# Ansible Ad-hoc Commands

## Step-01: Configuring ansible for running modules on `Localhost`

```
# Update the /etc/ansible/hosts file to add localhost
localhost ansible_connection=local

# Now, tell ansible the location of host file through /etc/ansible/ansible.cfg
# uncomment the following line
inventory      = /etc/ansible/hosts

# Supported plugins - Uncomment the following line
[inventory]
enable_plugins = host_list, script, auto, yaml, ini, toml
```

## Step-02: Ansible ad-hoc commands

### 2.1 Ansible ad-hoc command syntax

```
# Syntax
ansible <host_pattern> -m module <module_name> -a <arguments>

# Example
ansible localhost -m debug -a "msg='Hello there'"
```

### 2.2 Print a statement - `debug` module

- The `debug` module prints statements during playbook execution.
- Useful for debugging variables or expressions without necessarily halting the playbook.

```
ansible localhost -a "date"

ansible localhost -m command -a "uptime"

# Execute ansible adhoc command
ansible localhost -m debug -a "msg='Sample text'"

# Verbose mode
ansible localhost -m debug -a "msg='Sample text'" -v
```

### 2.3 Executing linux commands - `command` & `shell` module

- You can use `command` and `shell` modules

```
# Get the free memory details using command module (uses Python)
ansible localhost -m command -a "free -mh"

# Get the free memory details using shell module
ansible localhost -m shell -a "free -mh"

# Get the free memory details+date using shell module
ansible localhost -m shell -a "free -mh;date"
```

### 2.4 File Management modules - `file, stat, copy, lineinfile, blockinfile, template, fetch`

- **`file` module**
  - To create/delete a file or directory
  - To get the existing file information
  - To modify the file paramters like mode, owner etc.

```
# Create a file on the managed node
ansible all -m file -a "path='/tmp/test.txt' state='touch'"

# Create a file with custom permissions
ansible all -m file -a "path='/tmp/test1.txt' mode='0755' state='touch'"

# To verify the created files, list files using "command" module
ansible all -m command -a "ls -lrt /tmp"

# Change the permission of test1.txt file
ansible all -m file -a "path='/tmp/test1.txt' mode='0777'"

# Delete a file
ansible all -m file -a "path=/path/test1.txt' state='absent'"
```

- **`stat` module**

### 2.5 Package Management module - `yum, apt, pip`

```
ansible localhost -b -m yum -a "name='git' state='installed'"

ansible localhost -b -m yum -a "name='httpd' state='installed'"
```

### 2.6 Service Management modules - `service`

```
ansible localhost -b -m service -a "name='httpd' state='started'"

ansible localhost -b -m service -a "name='httpd' enabled='yes'"
```
