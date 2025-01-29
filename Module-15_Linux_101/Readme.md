# Linux Cheatsheet

## Contents

| S.No | Linux Commands Category     | Description |
|------|-----------------------------|-------------|
| 1    | System Information          |             |
| 2    | Harware Information         |             |
| 3    | User Management             |             |
| 4    | File & Directory Management |             |
| 5    | File Permissions            |             |
| 6    | Process Management          |             |
| 7    | Network                     |             |
| 8    | Compression/Archives        |             |
| 9    | Package Management          |             |
| 10   | Search                      |             |
| 11   | Login or Connectivity       |             |
| 12   | File Transfer               |             |

## 01. System Information

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

## 02. Hardware Information

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

## 03. User Management

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

## 04. File & Directory Management

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

## 05. File Permissions

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

## 06. Process Management

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

## 07. Network

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

## 08. Compression/Archives

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

## 09. Package Management

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

## 10. Search

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

## 11. Login or Connectivity

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

## 12. File Transfer

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
