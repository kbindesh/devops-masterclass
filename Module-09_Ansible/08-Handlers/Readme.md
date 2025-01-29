# Ansible Handlers

## Overview

- Sometimes you want a task to run only when a change is made on a machine.
- For example, you may want to restart a service if a task updates the configuration of that service, but not if the configuration is unchanged.
- Ansible uses handlers to achieve this funcationality.
- Handlers are tasks that only run when notified.

## Ansible Handler

### Example-01

```
---
- name: Setup apache webserver
  hosts: webservers
  vars:
    service_name: httpd
    http_port: 80
  become: yes
  tasks:
    - name: Install latest Apache webserver
      yum:
        name: "{{ service_name }}"
        state: latest
      notify: start apache webserver

  handlers:
    - name: start apache webserver
      service:
        name: "{{ service_name }}"
        state: started
```

### Example-02

### Example-03
