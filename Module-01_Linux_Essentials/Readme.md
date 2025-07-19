# *Linux Essentials* for Cloud and DevOps Engineers

## 01. Introduction to `Linux`

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

## 02. Basic Linux Commands

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

## 03. System Information

```
# Display Linux system information
uname -a

# Display kernel release information
uname -r

# Show operating system information such as distribution name and version
cat /etc/os-release
# Show how long the system has been running + load
uptime

# Show system host name
hostname

# Display all local IP addresses of the host.
hostname -I

# Show system reboot history
last reboot

# Show the current date and time
date

# Show this month's calendar
cal

# Display who is online
w

# Who you are logged in as
whoami
```

## 04. Hardware Information

```
# Display messages in kernel ring buffer
dmesg

# Display CPU information
cat /proc/cpuinfo

# Display memory information
cat /proc/meminfo

# Display free and used memory ( -h for human readable, -m for MB, -g for GB.)
free -h

# Display PCI devices
lspci -tv

# Display USB devices
lsusb -tv

# Display DMI/SMBIOS (hardware info) from the BIOS
dmidecode

# Show info about disk sda
hdparm -i /dev/sda

# Perform a read speed test on disk sda
hdparm -tT /dev/sda

# Test for unreadable blocks on disk sda
badblocks -s /dev/sda
```

## 05. User Management

```
# Display the user and group ids of your current user.
id

# Display the last users who have logged onto the system.
last

# Show who is logged into the system.
who

# Show who is logged in and what they are doing.
w

# Create a group named "test".
groupadd test

# Create an account named john, with a comment of "John Smith" and create the user's home directory.
useradd -c "John Smith" -m john

# Delete the john account.
userdel john

# Add the john account to the sales group
usermod -aG sales john
```

## 06. File & Directory Management

```
# List all files in a long listing (detailed) format
ls -al

# Display the present working directory
pwd

# Create a directory
mkdir directory

# Remove (delete) file
rm file

# Remove the directory and its contents recursively
rm -r directory

# Force removal of file without prompting for confirmation
rm -f file

# Forcefully remove directory recursively
rm -rf directory

# Copy file1 to file2
cp file1 file2

# Copy source_directory recursively to destination. If destination exists, copy source_directory into destination, otherwise create destination with the contents of source_directory.
cp -r source_directory destination

# Rename or move file1 to file2. If file2 is an existing directory, move file1 into directory file2
mv file1 file2

# Create symbolic link to linkname
ln -s /path/to/file linkname

# Create an empty file or update the access and modification times of file.
touch file

# View the contents of file
cat file

# Browse through a text file
less file

# Display the first 10 lines of file
head file

# Display the last 10 lines of file
tail file

# Display the last 10 lines of file and "follow" the file as it grows.
tail -f file
```

## 07. File Permissions

![image](https://github.com/kbindesh/devops-masterclass/assets/30317164/6dd466f2-5fb2-40b0-bed2-e2972d9f85eb)

```
  PERMISSION      EXAMPLE

         U   G   W
        rwx rwx rwx     chmod 777 filename
        rwx rwx r-x     chmod 775 filename
        rwx r-x r-x     chmod 755 filename
        rw- rw- r--     chmod 664 filename
        rw- r-- r--     chmod 644 filename

# NOTE: Use 777 sparingly!

        LEGEND
        U = User
        G = Group
        W = World

        r = Read
        w = write
        x = execute
        - = no access
```

## 08. Process Management

```
# Display your currently running processes
ps

# Display all the currently running processes on the system.
ps -ef

# Display process information for processname
ps -ef | grep processname

# Display and manage the top processes
top

# Interactive process viewer (top alternative)
htop

# Kill process with process ID of pid
kill pid

# Kill all processes named processname
killall processname

# Start program in the background
program &

# Display stopped or background jobs
bg
```

## 09. Networking

```
# Display all network interfaces and IP address
ip a

# Display eth0 address and details
ip addr show dev eth0

# Query or control network driver and hardware settings
ethtool eth0

# Send ICMP echo request to host
ping host

# Display whois information for domain
whois domain

# Display DNS information for domain
dig domain

# Reverse lookup of IP_ADDRESS
dig -x IP_ADDRESS

# Display DNS IP address for domain
host domain

# Display the network address of the host name.
hostname -i

# Display all local IP addresses of the host.
hostname -I

# Download http://bindeshtutorials.com/file
wget http://bindeshtutorials.com/file

# Display listening tcp and udp ports and corresponding programs
netstat -nutlp
```

## 10. Compression/Archives

```
# Create tar named archive.tar containing directory.
tar cf archive.tar directory

# Extract the contents from archive.tar.
tar xf archive.tar

# Create a gzip compressed tar file name archive.tar.gz.
tar czf archive.tar.gz directory

# Extract a gzip compressed tar file.
tar xzf archive.tar.gz

# Create a tar file with bzip2 compression
tar cjf archive.tar.bz2 directory

# Extract a bzip2 compressed tar file.
tar xjf archive.tar.bz2
```

## 11. Package Management

```
# Search for a package by keyword.
yum search keyword

# Install package.
yum install package

# Display description and summary information about package.
yum info package

# Install package from local file named package.rpm
rpm -i package.rpm

# Remove/uninstall package.
yum remove package

# Install software from source code.
tar zxvf sourcecode.tar.gz

cd sourcecode

./configure

make

make install
```

## 12. Searching

```
# Search for pattern in file
grep pattern file

# To search for every line that contains the word GNU
grep "GNU" GPL-3

# Search recursively for pattern in directory
grep -r pattern directory

# Find files and directories by name
locate name

# Find files in /home/john that start with "prefix".
find /home/john -name 'prefix*'

# Find files larger than 100MB in /home
find /home -size +100M
```

## 13. Login or Connectivity

```
# Connect to host as your local username.
ssh host

# Connect to host as user
ssh user@host

# Connect to host using port
ssh -p port user@host

## Connect to remote linux host using keypair
ssh -i <keypair> username@public_ip_or_dns_name

```

## 14. File Transfer

```
# Secure copy file.txt to the /tmp folder on server
scp file.txt server:/tmp

# Copy *.html files from server to the local /tmp folder.
scp server:/var/www/*.html /tmp

# Copy all files and directories recursively from server to the current system's /tmp folder.
scp -r server:/var/www /tmp

# Synchronize /home to /backups/home
rsync -a /home /backups/

# Synchronize files/directories between the local and remote system with compression enabled
rsync -avz /home server:/backups/
```

