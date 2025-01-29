# Ansible Inventory

## 01. What is an Ansible `Hosts` file?

- Ansible Host file (also known as inventory) defines the managed nodes configurations that you automate, with groups so you can run automation tasks on multiple hosts at the same time.
- Once your inventory is defined, you use patterns to select the hosts or groups you want Ansible to run actions on it.
- The simplest inventory is a single file with a list of hosts and groups.
- The default location for this file is <b>_/etc/ansible/hosts_</b>.
- You can specify a different inventory file at the command line using the -i <path> option or in configuration using inventory.
- The most common inventory file formats are:
  - <b>_INI_</b>
  - <b>_YAML_</b>
- Sample inventory file

  ```
    appserver.novatec.com

    [webservers]
    webserver1.novatec.com
    webserver2.novatec.com
    webserver3.novatec.com

    [dbservers]
    dbserver1.novatec.com
    dbserver2.novatec.com
  ```

## 02. How to connect to remote host using Ansible inventory file (INI/YAML) ?

```
# With inventory in INI format
ansible -i 02-sample-inventory.ini -m ping
```

```
# With inventory in YAML format
ansible -i 04-sample-inventory.yaml -m ping
```

## 03. Passing multiple inventory sources

- You can target multiple inventory sources at the same time by giving multiple inventory parameters from the command line or by configuring ANSIBLE_INVENTORY.
- This can be useful when you want to target normally separate environments, like staging and production, at the same time for a specific action.
- To target two inventory sources from the command line:

```
ansible-playbook get_logs.yml -i staging-inventory.yml -i prod-inventory.yml
```

## 04. Organizing inventory in a custom directory

- You can consolidate multiple inventory sources in a single directory. The simplest version of this is a directory with multiple files instead of a single inventory file.
- A single file gets difficult to maintain when it gets too long.
- If you have multiple teams and multiple automation projects, having one inventory file per team or project lets everyone easily find the hosts and groups that matter to them.
- You can also combine multiple inventory source types in an inventory directory.
- This can be useful for combining static and dynamic hosts and managing them as one inventory.
- The following inventory directory combines an inventory plugin source, a dynamic inventory script, and a file with static hosts:
  ```
  inventory/
     openstack.yml          # configure inventory plugin to get hosts from OpenStack cloud
     dynamic-inventory.py   # add additional hosts with dynamic inventory script
     on-prem                # add static hosts and groups
     parent-groups          # add static hosts and groups
  ```
- You can also configure the inventory directory in your _ansible.cfg_

## 05. Adding variables to the inventory file

- https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html#connecting-to-hosts-behavioral-inventory-parameters

## 06. Assigning variables to many hosts: Group Variables

- If all hosts in a group share a variable value, you can apply that variable to an entire group at once.
- In INI inventory file, it will be like:

  ```
  [mumbaiServers]
     host1
     host2

  [mumbaiServers:vars]
     smtp_server=smtp.mumbai.novatec.com
     proxy=proxy.mumbai.novatec.com
  ```

- In YAML inventory file, it will be like:
  ```
   mumbai:
     hosts:
       host1:
       host2:
     vars:
       smtp_server: smtp.mumbai.novatec.com
       proxy: proxy.mumbai.novatec.com
  ```

## 07. [Ansible Inventory Parameters (Variables)](https://github.com/novatecstack/ansible-masterclass/blob/main/Module-05_Ansible_Inventory/inventory-variables.md)

## 09. Reference Links

- [Ansible Inventory Official Documentation](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html)
