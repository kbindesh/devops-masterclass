# Linux Questions

## Linux Fundamentals

- How will you get the `Name` and the `UID` of the `docker` user?

- How to list all files, including hidden ones, in a directory?

- What is the Unix/Linux command to remove a directory and its - contents?

- Which command will show you free/used memory? Does free - memory exist on Linux?

- How to search for the string "linux is everywhere" in files of a directory recursively?

- How to connect to a remote server or what is SSH?

- How to get all environment variables and how can you use them?

- I'm getting "**command not found**" when I run ifconfig -a. What is wrong here and how will you fix it?

- What happens if I type TAB-TAB on terminal?
- What command will show the available disk space on the Unix/- Linux system?
- What commands do you know that can be used to check DNS - records?
- What Unix/Linux commands will alter a files ownership, files - permissions?
- What does chmod +x FILENAME do?

- What does the permission 0750 on a file mean?

- What does the permission 0750 on a directory mean?
- How to add a new system user without login permissions?
- How to add/remove a group from a user?
- What is a bash alias?
- How do you set the mail address of the root/a user?
- What does CTRL-c do?
- What does CTRL-d do?
- What does CTRL-z do?
- What is in /etc/services?
- How to redirect STDOUT and STDERR in bash? (> /dev/null 2>&1)
- What is the difference between UNIX and Linux.
- What is the difference between Telnet and SSH?
  Explain the three load averages and what do they indicate. - What command can be used to view the load averages?
  Can you name a lower-case letter that is not a valid option - for GNU ls?
- What is a Linux kernel module?
  Walk me through the steps in booting into single user mode to - troubleshoot a problem.
  Walk me through the steps you'd take to troubleshoot a 404 - error on a web application you administer.
- What is ICMP protocol? Why do you need to use?

- How will you change the ownership and permissions of a file or directory in Linux?

  - chown
  - chmod

- How do you manage and view running processes in Linux?

  - ps | ps -aux
  - top - resource utilization by processes (cpu, memory)

- What is SSH?

  - Explain about protocol in 1-2 sentences.
  - Explain the command for connecting to the

- How would you check memory and cpu stats as a Linux Admin?

  - free: for memory stats
  - top and htop: for CPU stats

- What is a `Cronjob`?

- How will you Unpack/Unzip test.tar.gz without man pages or google.

- Remove all "\_.pyc" files from testdir recursively?
- Search for "hello world" in all \_.py files.
- Replace the occurrence of "hello world" with "Hello Buddy" in all \*.txt files.
- Test if port 443 on a machine with IP address X.X.X.X is reachable.

## Linux Intermediate-level Questions

- What do the following commands do and how would you use them?
  - tee
  - awk
  - tr
  - cut
  - tac
  - curl
  - wget
  - watch
  - head
  - tail
  - less
  - cat
  - touch
  - sar
  - netstat
  - tcpdump
  - lsof
- What does an & after a command do?

- What does & disown after a command do?

- What is a packet filter and how does it work?

- What is Virtual Memory?

- What is swap and what is it used for?
- What is an A record, an NS record, a PTR record, a CNAME record, an MX - record?
- Are there any other RRs and what are they used for?
- What is a Split-Horizon DNS?
- What is the sticky bit?
- What does the immutable bit do to a file?
- What is the difference between hardlinks and symlinks? What happens when you remove the source to a symlink/hardlink?
- What is an inode and what fields are stored in an inode?
- How to force/trigger a file system check on next reboot?
- What is SNMP and what is it used for?
- What is a runlevel and how to get the current runlevel?
- What is SSH port forwarding?
- What is the difference between local and remote port forwarding?
- What are the steps to add a user to a system without using useradd/- adduser?
- What is MAJOR and MINOR numbers of special files?
- Describe the mknod command and when you'd use it.
- Describe a scenario when you get a "filesystem is full" error, but 'df' - shows there is free space.
- Describe a scenario when deleting a file, but 'df' not showing the - space being freed.
- Describe how 'ps' works.
- What happens to a child process that dies and has no parent process to - wait for it and what’s bad about this?
- Explain briefly each one of the process states.
- How to know which process listens on a specific port?
- What is a zombie process and what could be the cause of it?
- You run a bash script and you want to see its output on your terminal and save it to a file at the same time. How could you do it?
- Explain what echo "1" > /proc/sys/net/ipv4/ip_forward does.
- Describe briefly the steps you need to take in order to create and - install a valid certificate for the site https://foo.example.com.
- Can you have several HTTPS virtual hosts sharing the same IP?
- What is a wildcard certificate?
- Which Linux file types do you know?
- What is the difference between a process and a thread? And parent and child processes after a fork system call?
- What is the difference between exec and fork?
- What is "**nohup**" used for?
- What is the difference between these two commands?
  - myvar=hello
  - export myvar=hello
- How many NTP servers would you configure in your local ntp.conf?
- What does the column 'reach' mean in ntpq -p output?
- You need to upgrade kernel at 100-1000 servers, how you would do this?
- How can you get Host, Channel, ID, LUN of SCSI disk?
- How can you limit process memory usage?
- What is bash quick substitution/caret replace(^x^y)?
- Do you know of any alternative shells? If so, have you used any?
- What is a tarpipe (or, how would you go about copying everything, - including hardlinks and special files, from one server to another)?
- How can you tell if the httpd package was already installed?
- How can you list the contents of a package?
- How can you determine which package is better: openssh-server-5.3p1-118.- 1.el6_8.x86_64 or openssh-server-6.6p1-1.el6.x86_64 ?
- Can you explain to me the difference between block based, and object - based storage?
