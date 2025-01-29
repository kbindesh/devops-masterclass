# Linux for Cloud and DevOps Engineers

## 01. Introduction to Linux

### 1.1 What is Linux?

- Just like Windows, iOS, and Mac OS, Linux is an operating system.
- It was devolped by Linus Torvalds.
- It comes from Unix family.
- Linux is compatible with most of the hardware architectures like x86, ARM etc.
- For more details, refer https://www.linux.com/what-is-linux/.

### 1.2 Linux Distributions

- Linux has a number of different flavors of linux which suit a particular type of user/requirement.
- From new users to experienced ones, you will find a flavor of linux, which suits to your need.
- These versions are called distributions (or in the short, "distros").

- Popular Linux distributions include:

  - Ubuntu

  - Fedora
  - Amazon Linux
  - CentOS
  - Alma Linux
  - RHEL
  - Debian

### 1.3 Linux File systems

- Linux file system is generally used to handle the data management of the storage.
- It helps to arrange the file on the disk storage.
- It manages the file name, file size, creation date, and much more information about a file.
- In Linux, everything is considerd as a file.
- Even the devices attached to your machines are also represented as files.
- The files are stored in a directory (in windows systems, we call it folder), and every directory contains a file with a tree structure, called **file system hierarchy**.
- Linux uses single rooted, inverted tree like structure.
- Root directory represents with / (forward slash) and is a top-level directory in linux.

- The below table gives well-known top-level Linux directory list with description:

  - **/ (root)**: It is the top-level filesystem directory. It must include every file needed to boot the Linux system before another filesystem is mounted. Every other filesystem is mounted on a well-defined and standard mount point because of the root filesystem directories after the system is started.

  - **/boot**: It includes the static kernel and bootloader configuration and executable files needed to start a Linux computer.
  - /bin: This directory includes user executable files.
  - /dev: It includes the device file for all hardware devices connected to the system. These aren't device drivers; instead, they are files that indicate all devices on the system and provide access to these devices.
  - **/etc**: It includes the local system configuration files for the host system.
  - **/lib**: It includes shared library files that are needed to start the system.
  - **/home**: The home directory storage is available for user files. All users have a subdirectory inside /home.
  - **/mnt**: It is a temporary mount point for basic filesystems that can be used at the time when the administrator is working or repairing a filesystem.
  - **/media**: A place for mounting external removable media devices like USB thumb drives that might be linked to the host.
  - **/opt**: It contains optional files like vendor supplied application programs that must be placed here.
  - **/root**: It's the home directory for a root user. Keep in mind that it's not the '/' (root) file system.
  - **/tmp**: It is a temporary directory used by the OS and several programs for storing temporary files. Also, users may temporarily store files here. Remember that files may be removed without prior notice at any time in this directory.
  - **/sbin**: These are system binary files. They are executables utilized for system administration.
  - **/usr**: They are read-only and shareable files, including executable libraries and binaries, man files, and several documentation types.
  - **/var**: Here, variable data files are saved. It can contain things such as MySQL, log files, other database files, email inboxes, web server data files, and much more.

### 1.4 Setting-up Linux machine in AWS (EC2 Instance)

- Sign-in to **AWS Management console**, https://console.aws.amazon.com/.
- Navigate to **EC2** service >> Click **Launch Instances** button.
  - **Name**: <name_of_the_instance>
  - **AMI**: Amazon Linux 2
  - **Instance Type**: t2.micro
  - **Key Pair**: <create_a_new_keypair>
  - **Network settings (VPC, Subnet, Public IP)**: <leave_to_defaults>
  - **Firewall (SG)**: Allow ingress on 22 (SSH) for all IPv4
  - **Storage**: <leave_to_defaults>

### 1.5 Connecting to Linux machine

- You can connect to any remote linux machine in multiple ways:
  1. Using AWS EC2 Launch Connect
  2. Using AWS CloudShell
  3. Using **ssh** utility (from your local windows/linux/mac machine)
  4. Using any external SSH clients (mobaxterm, putty etc)

## 01. Basic Commands

| Command      | Description                                                             |
| :----------- | :---------------------------------------------------------------------- |
| **man**      | Shows manual of the command                                             |
| **hostname** | Displays hostname of the system                                         |
| **clear**    | Clear the screen                                                        |
| **date**     | Displays the current date and time                                      |
| **cal**      | Displays current month's calendar                                       |
| **uptime**   | Displays how long the system has been running                           |
| **whoami**   | Displays the username of the effective user currently running the shell |
| **finger**   | Get the details of the user                                             |
| **who**      | Displays information about all the currently logged-in users            |

## 02. Managing Files and Directories

## 03. System Management

## 04. User Management

## 05. Service Management

## 06. Package Management

## 07. Network Management

## 08. Process Management
