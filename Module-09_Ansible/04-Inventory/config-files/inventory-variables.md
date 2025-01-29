# [Ansible Inventory Variables](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html#connecting-to-hosts-behavioral-inventory-parameters)
Following variables control how Ansible interacts with remote hosts:

  - <b>*ansible_connection*</b></br>
    Connection type to the host. This can be the name of any of ansible’s connection plugins. SSH protocol types are smart, ssh or paramiko. The default is smart. 
General for all connections:
  - <b>*ansible_host*</b></br>
    The name of the host to connect to, if different from the alias you wish to give to it.

  - <b>*ansible_port*</b></br>
    The connection port number, if not the default (22 for ssh)

  - <b>*ansible_user*</b></br>
The user name to use when connecting to the host

  - <b>*ansible_password*</b></br>
The password to use to authenticate to the host (never store this variable in plain text; always use a vault. See Keep vaulted variables safely visible)
Specific to the SSH connection:

  - <b>*ansible_ssh_private_key_file*</b></br>
Private key file used by ssh. Useful if using multiple keys and you don’t want to use SSH agent.

  - <b>*ansible_ssh_common_args*</b></br>
This setting is always appended to the default command line for sftp, scp, and ssh. Useful to configure a ProxyCommand for a certain host (or group).

  - <b>*ansible_sftp_extra_args*</b></br>
This setting is always appended to the default sftp command line.

  - <b>*ansible_scp_extra_args*</b></br>
This setting is always appended to the default scp command line.

  - <b>*ansible_ssh_extra_args*</b></br>
This setting is always appended to the default ssh command line.

  - <b>*ansible_ssh_pipelining*</b></br>
Determines whether or not to use SSH pipelining. This can override the pipelining setting in ansible.cfg.

  - <b>*ansible_ssh_executable (added in version 2.2)*</b></br>
This setting overrides the default behavior to use the system ssh. This can override the ssh_executable setting in ansible.cfg.
Privilege escalation (see Ansible Privilege Escalation for further details):

  - <b>*ansible_become*</b></br>
Equivalent to ansible_sudo or ansible_su, allows to force privilege escalation

  - <b>*ansible_become_method*</b></br>
Allows to set privilege escalation method

  - <b>*ansible_become_user*</b></br>
Equivalent to ansible_sudo_user or ansible_su_user, allows to set the user you become through privilege escalation

  - <b>*ansible_become_password*</b></br>
Equivalent to ansible_sudo_password or ansible_su_password, allows you to set the privilege escalation password (never store this variable in plain text; always use a vault. See [Keep vaulted variables safely visible](https://docs.ansible.com/ansible/latest/tips_tricks/ansible_tips_tricks.html#tip-for-variables-and-vaults))

  - <b>*ansible_become_exe*</b></br>
Equivalent to ansible_sudo_exe or ansible_su_exe, allows you to set the executable for the escalation method selected

  - <b>*ansible_become_flags*</b></br>
Equivalent to ansible_sudo_flags or ansible_su_flags, allows you to set the flags passed to the selected escalation method. This can be also set globally in ansible.cfg in the sudo_flags option
Remote host environment parameters:

  - <b>*ansible_shell_type*</b></br>
The shell type of the target system. You should not use this setting unless you have set the ansible_shell_executable to a non-Bourne (sh) compatible shell. By default commands are formatted using sh-style syntax. Setting this to csh or fish will cause commands executed on target systems to follow those shell’s syntax instead.

  - <b>*ansible_python_interpreter*</b></br>
The target host python path. This is useful for systems with more than one Python or not located at /usr/bin/python such as *BSD, or where /usr/bin/python is not a 2.X series Python. We do not use the /usr/bin/env mechanism as that requires the remote user’s path to be set right and also assumes the python executable is named python, where the executable might be named something like python2.6.
