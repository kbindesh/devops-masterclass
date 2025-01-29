# Setup and Integate Sonatype Nexus with Jenkins

## Step-XX: Setup Nexus Server

### System Requirments

Before starting, ensure your system meets the following requirements:

- **RAM**: Minimum 2GB
- **CPU**: At least 1 cores
- **Java**: OpenJDK 17 (or the version required by the latest Nexus release)

### Provision an EC2 Instance (or any other VM instance)

- **Name**: NEXUS-SERVER
- **AMI**: Amazon Linux 2
- **Instance type**: t3.medium
- **Security Group**
  - Ingress: Allow 22 (ssh), 8081 (nexus)

### Setup Nexus server

- **Install Java**

```
# Install Java-17
sudo yum install -y java-17-amazon-corretto.x86_64

# To check the installed java version
java --version
```

- **Download and Install Nexus**

```
# Switch to /opt directory to setup nexus
cd /opt

# Download the nexus package from official site
sudo wget https://download.sonatype.com/nexus/3/nexus-3.76.1-01-unix.tar.gz

[For more details: https://help.sonatype.com/en/download.html]
```

- **(Optional) Verify MD5 Checksum**

```
md5sum nexus-3.76.1-01-unix.tar.gz
```

- **Extract and rename nexus directory**

```
sudo tar -zxvf nexus-3.76.1-01-unix.tar.gz

sudo mv nexus-3.76.1-01 nexus
```

- **Create a new user for Nexus ops**

```
# Create an exclusive user for Nexus
sudo useradd nexus

# Set a password for the user
sudo passwd nexus
```

- **Add the _nexus_ user to sudoers**

```
# Change /etc/sudoers
sudo chmod 755 /etc/sudoers

# Edit the sudoers file
sudo vi /etc/sudoers

# Add following line under "User privilege specification" after root user
nexus ALL=(ALL) NOPASSWD:ALL
```

- **Elevate the ownership of nexus directories**

```
# Change the ownership of Nexus directories to nexus user
sudo chown -R nexus:nexus /opt/nexus
sudo chown -R nexus:nexus /opt/sonatype-work
```

- **Set the user to run Nexus**

```
# Edit the nexus.rc file
sudo vi /opt/nexus/bin/nexus.rc

# Uncomment and set
run_as_user="nexus"
```

- **Create a Systemd service for Nexus**

```
# Create a systemd unit file
sudo vi /etc/systemd/system/nexus.service

# Add the following contents to the file created in the preceding command
[Unit]
Description=Nexus Service
After=network.target

[Service]
Type=forking
LimitNOFILE=65536
ExecStart=/opt/nexus/bin/nexus start
ExecStop=/opt/nexus/bin/nexus stop
User=nexus
Restart=on-abort

[Install]
WantedBy=multi-user.target
```

- **Update the /opt/nexus/bin/nexus.vmoptions**

```
sudo vi /opt/nexus/bin/nexus.vmoptions

# Update the java heap size
-Xmx1024m
-Xms1024m
```

- **Start the Nexus service**

```
# Reload systemd and start nexus service
sudo systemctl daemon-reload
sudo systemctl start nexus

# Enable nexus to start on boot
sudo systemctl enable nexus

# Check nexus service status | Should be in running state
sudo systemctl status nexus
```

### Access Nexus Web UI

- Open your web browser and navigate to: **http://<your-server-ip>:8081**.

- Click-on **Sign-in** button (top-right corner)

  - **Username**: admin
  - **Password**: Get the password from /opt/sonatype-work/nexus3/admin.password

- Set a new password for nexus

## Step-XX: Setup Jenkins Server with Maven

### Create an EC2 Instance

### Install & Configure Jenkins

### Install required Jenkins Plugins

### Add location of Java & Maven tools on Jenkins server

### Store Nexus server credentials on Jenkins server

## Step-XX: Develop Maven Project

## Step-XX: Update pom.xml file for Nexus integration

## Step-XX: Create settings.xml for Nexus specifications

## Step-XX: Create Jenkinsfile

## Step-XX: Create Jenkins Job
