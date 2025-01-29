# Registering Variables

- Many times, we need to set the value of a variable based on the result of a task.
- To use these results anywhere later in our playbook, you create a registered variable using the **register** clause when invoking a module.

## Capturing the output of a command to a variable

- **Example-01**

```
- name: Capturing the logged-in user
  hosts: clientnode
  tasks:
    - name: Capture output of whoami command
      ansible.builtin.command: whoami
      register: login
```

- **Example-02**

```
---
- name: Show return value of command module
  hosts: fedora
  gather_facts: false
  tasks:
    - name: Capture output of id command
      command: id -un
      register: login
    - debug: var=login
    - debug: msg="Logged in as user {{ login.stdout }}"
```
