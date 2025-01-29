# Ansible Variables

## 01. Types of Ansible Variables

- Custom variables
- Registered variables
- Fact variables
- Inventory variables
- Default variables

## 02: How to define a variable in Ansible?

```
# Syntax
vars:
  key: value

# Example
vars:
  username: bindesh
  num: 10
  height: 6.2
```

## 03. Sample playbook with Ansible variables

```
---
- name: Ansible variables play
  hosts: localhost
  vars:

  tasks:
    - name:
```
