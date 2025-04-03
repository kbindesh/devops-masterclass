# Setup and Integate Sonatype Nexus with Jenkins

## Step-01: Setup Nexus Server

### 1.1 System Requirments

Before starting, ensure your system meets the following requirements:

- **RAM**: Minimum 2GB
- **CPU**: At least 1 core
- **Java**: OpenJDK 17 (or the version required by the latest Nexus release)

### 1.2 Provision an EC2 Instance (or any other VM instance)

- **Name**: NEXUS-SERVER
- **AMI**: Amazon Linux 2
- **Instance type**: t3.medium
- **Security Group**
  - Ingress: Allow 22 (ssh), 8081 (nexus)

### 1.3 Setup Nexus server

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

### 1.4 Access Nexus Web UI

- Open your web browser and navigate to: **http://<your-server-ip>:8081**.

- Click-on **Sign-in** button (top-right corner)

  - **Username**: admin
  - **Password**: Get the password from /opt/sonatype-work/nexus3/admin.password

- Set a new password for nexus

## Step-02: Create a Nexus Repositories (snapshot, release)

- Navigate to Nexus dashboard as an admin user
- Click the gear icon on the upper toolbar >> click Repositories >> Click **Create Repository** button
- **Repository-01**

  - Name: bin-mvnapp-SNAPSHOT
  - Version Policy: Snapshot
  - [*Leave rest of the settings to default*]

- **Repository-02**
  - Name: bin-mvnapp-RELEASE
  - Version Policy: Release
  - [*Leave rest of the settings to default*]

## Step-03: Setup Jenkins Server

### 3.1 Create an EC2 Instance and Configure

- [Setup Jenkins server on Linux (Amazon Linux 2)](https://github.com/kbindesh/jenkins-masterclass/tree/main/Module-03_Setting_up_Jenkins/01-jenkins-on-amazon-linux)

### 3.2 Install & Configure Maven on Jenkins server

- [Setup Maven on Linux (Amazon Linux 2)](https://github.com/kbindesh/maven-bootcamp/blob/main/Module-02_Setting_up_Maven_Environment/01-setup-mvn-on-amzn-linux-2.md)

### 3.3 Install required Jenkins Plugins

- Maven Invoker
- Maven Integration
- **Nexus Artifact Uploader**
- Pipeline: Stage view
- SonarQube Scanner
- Pipeline Utility Steps
- **Script Security Plugin** (For using readMavenPom() function in Jenkinsfile)

### 3.4 Add location of Java & Maven tools on Jenkins server

- Jenkins Dashboard >> Manage Jenkins >> **Tools**

- **JDK Installations**

  - Name: JDK-17
  - Location: /usr/lib/jvm/java-17-amazon-corretto.x86_64

- **Maven Installations**

  - Name: Maven-3.9.8
  - Location: /opt/apache-maven-3.9.8

### 3.5 Adding Nexus server credentials to Jenkins

- Jenkins Dashboard >> Manage Jenkins >> Credentials >> Global
  - Kind: Username & Password
  - Scope: Global
  - Username: admin
  - Password: <your_nexus_server_password>
  - ID: **nexus**

## Step-04: Develop Maven Project

- The sample maven application used in this tutorial is a basic java application.
- You may clone the sample app repo from https://github.com/kbindesh/jenkins-pipeline-lab/tree/master

```
git clone https://github.com/kbindesh/jenkins-pipeline-lab/tree/master
```

## Step-05: Update the Jenkinsfile (with nexus stage)

- **Note**: Kindly replace the placeholder on line #14 with your _nexus server ip address_ and line #16 with your _nexus repository name_.

```
pipeline {
  agent any

  tools {
    maven 'Maven-3.9.8'
    jdk 'Java-17'
  }

  environment {
    MVN_ARTIFACT_ID = readMavenPom().getArtifactId()
    MVN_APP_VERSION = readMavenPom().getVersion()
    MVN_GROUP_ID = readMavenPom().getGroupId()
    ARTIFACT_FILE_TYPE = 'jar'
    NEXUS_SERVER_URL = '<nexus_server_private_ip>:8081'
    NEXUS_VERSION = 'nexus3'
    NEXUS_REPO_NAME = 'bin-mvnapp-SNAPSHOT'
    NEXUS_PROTOCOL = 'http'
  }

  stages{
    stage('Unit Testing - JUnit'){
      steps{
        sh 'mvn test'
      }
      post {
        always {
          junit 'target/surefire-reports/*.xml'
        }
      }
    }
    stage('Code Review - SonarQube'){
      steps{
        echo 'Performaing static code analysis..'
      }
    }
    stage('Package Application - Maven'){
      steps{
        sh 'mvn clean package -DskipTests=true'
        archiveArtifacts artifacts: 'target/*.jar'
      }
    }
    stage('Publish Artifacts - Nexus'){
      steps{
        nexusArtifactUploader artifacts: [[artifactId: '${MVN_ARTIFACT_ID}', classifier: '', file: '${MVN_ARTIFACT_ID}-${MVN_APP_VERSION}.jar', type: '${ARTIFACT_FILE_TYPE}']], credentialsId: 'nexus', groupId: '${MVN_GROUP_ID}', nexusUrl: '${NEXUS_SERVER_URL}', nexusVersion: '${NEXUS_VERSION}', protocol: '${NEXUS_PROTOCOL}', repository: '${NEXUS_REPO_NAME}', version: '${MVN_APP_VERSION}'
      }
    }
  }
}

```

## Step-06: Push the changes on GitHub

```
git add .

git commit -m "Maven App with Nexus Integration v1.0"

git remote add origin <your_github_repo_url>

git push -u origin master
```

## Step-07: Create Jenkins Job

- Jenkins Dashboard >> New Item
  - Name: mvn-nexus-integration-lab
  - Type: Pipeline
  - Description: Jenkins job for publishing artifacts to Nexus
  - Pipeline
    - Definition: Pipeline script from SCM
    - SCM: Git
    - Repository URL: <your_github_repo_url>
    - Credentials: <leave_blank_if_repo_is_public>
    - Branches to build: master
    - Script Path: Jenkinsfile

## Step-08: Verify the published artifacts on Nexus

- Navigate to Nexus server dashboard >> Repositories >> Select the snapshot repository we created in the earlier step.
- You should see the maven package with \*.jar file.

## References

- [Maven POM file](https://maven.apache.org/pom.html)
