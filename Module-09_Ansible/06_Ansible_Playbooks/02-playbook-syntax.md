```
---
- name: play-1
  hosts: localhost
  tasks:
    - name: play-1-task-1
      ansible.builtin.debug:
        msg:
          - "Ansible is awesome"
    - name: play-1-task-2
      ansible.builtin.debug:
        msg:
          - "Ansible contributes in DevOps"

- name: play-2
  hosts: localhost
  tasks:
    - name: play-2-task-1
      ansible.builtin.debug:
        msg:
          - "Ansible is awesome"
    - name: play-2-task-2
      ansible.builtin.debug:
        msg:
          - "Ansible contributes in DevOps"
```
