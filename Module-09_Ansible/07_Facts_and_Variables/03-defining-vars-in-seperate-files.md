# Defining Variables in separate files

# Define variables in variables file (`vars_files` section)

- Ansible also allows you to put variables into one or more files, which can then be referenced in the playbook using a section called **vars_files**.

- The playbook with external variable file referenced, say nginx-playbook.yml will look something like this:

```
---
- name: Demonstrating vars in a File
  hosts: localhost
  vars_files:
    - nginx_vars.yml
  tasks:
    ...
```

- The **ngnix_vars.yml** file will look something like this:

```
key_file: nginx.key
cert_file: nginx.crt
conf_file: /etc/nginx/sites-available/default
server_name: localhost
```
