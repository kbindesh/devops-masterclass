# Ansible Modules

- <b>_Ansible Modules_</b> are discrete units of code that can be used from the command line or in a playbook task.
- Ansible executes each module, usually on the remote managed node, and collects return values.

## 01. Getting the list of all modules

```
ansible-doc -l

ansible-doc -l | grep <module_name>

# Get documentation for a particular module
ansible-doc <module_name>
```

## 02. Ansible modules - Reference

- [Ansible Module Index](https://docs.ansible.com/ansible/2.8/modules/modules_by_category.html)

## 03. Commonly used Ansible modules

- `debug` module (https://docs.ansible.com/ansible/latest/collections/ansible/builtin/debug_module.html)
- `yum` module (https://docs.ansible.com/ansible/2.8/modules/yum_module.html#yum-module)
- `apt` module (https://docs.ansible.com/ansible/2.8/modules/apt_module.html#apt-module)
- `dnf` module (https://docs.ansible.com/ansible/2.8/modules/dnf_module.html#dnf-module)
- `pip` module (https://docs.ansible.com/ansible/2.8/modules/pip_module.html#pip-module)
- `service` module (https://docs.ansible.com/ansible/2.8/modules/service_module.html)
- `copy` module (https://docs.ansible.com/ansible/2.8/modules/copy_module.html#copy-module)
- `command` module (https://docs.ansible.com/ansible/2.8/modules/command_module.html#command-module)
- `shell` module (https://docs.ansible.com/ansible/2.8/modules/shell_module.html#shell-module)
- `script` module (https://docs.ansible.com/ansible/2.8/modules/script_module.html#script-module)
- `lineinfile` module (https://docs.ansible.com/ansible/2.8/modules/lineinfile_module.html#lineinfile-module)
- `blockinfile` modules (https://docs.ansible.com/ansible/2.8/modules/blockinfile_module.html#blockinfile-module)
- `stat` module (https://docs.ansible.com/ansible/2.8/modules/stat_module.html#stat-module)
- `cron` module (https://docs.ansible.com/ansible/latest/collections/ansible/builtin/cron_module.html)
- `docker` modules (https://docs.ansible.com/ansible/latest/collections/community/docker/index.html)
