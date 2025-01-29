# Setup Prometheus server on Amazon Linux EC2 instance

## Prerequisites

- AWS Account

## Step-01: Install and configure `Prometheus` (self-hosted) on Amazon EC2 instance

### 1.1 - Prerequisites

- AWS Account

### 1.2 - Create an Amazon EC2 instance for `Prometheus server`

- Name: Prometheus-Server
- AMI: Amazon Linux 2 (you may use any other supported distro)
- Instance type: t2.micro
- Key: <create_new_keypair>
- VPC and Subnet: <leave_to_default>
- Security Group: <create_new_sg>
  - Name: Prometheus-SG
  - Ingress: Allow 22 (SSH), 9090 (Prometheus) from any IPv4 address
  - Description: Prometheus server security group

### 1.3 - Install and configure `Prometheus`

- SSH to prometheus server (ec2 instance) created in the preceding step and execute the following steps:

```
# Create a new user for prometheus ops
sudo useradd --no-create-home prometheus

# Create following directories for prometheus config
sudo mkdir /etc/prometheus
sudo mkdir /var/lib/prometheus

# Download Prometheus
wget https://github.com/prometheus/prometheus/releases/download/v2.19.0/prometheus-2.19.0.linux-amd64.tar.gz

# Extract the downloaded tarball
tar xvfz prometheus-2.19.0.linux-amd64.tar.gz
```

- **Copy the _Prometheus_ and _Promtool_ files to respective locations**

```
sudo cp prometheus-2.19.0.linux-amd64/prometheus /usr/local/bin
sudo cp prometheus-2.19.0.linux-amd64/promtool /usr/local/bin/
sudo cp -r prometheus-2.19.0.linux-amd64/consoles /etc/prometheus
sudo cp -r prometheus-2.19.0.linux-amd64/console_libraries /etc/prometheus
sudo cp prometheus-2.19.0.linux-amd64/promtool /usr/local/bin/
```

- **Remove the tarball from system**

```
rm -rf prometheus-2.19.0.linux-amd64.tar.gz prometheus-2.19.0.linux-amd64
```

- **Create a Prometheus configuration file `prometheus.yml` on location `/etc/prometheus`**

```
# Create prometheus.yml file
sudo vi /etc/prometheus/prometheus.yml

# Add the following specs to the above created prometheus.yml file
global:
  scrape_interval: 15s
  external_labels:
    monitor: 'prometheus'

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']
```

- **Create a file `prometheus.service` for Prometheus service on location `/etc/systemd/system`**

```
# Create the prometheus.service file
sudo vi /etc/systemd/system/prometheus.service

# Add the following specs to the above created prometheus.service file
[Unit]
Description=Prometheus
Wants=network-online.target
After=network-online.target

[Service]
User=prometheus
Group=prometheus
Type=simple
ExecStart=/usr/local/bin/prometheus \
    --config.file /etc/prometheus/prometheus.yml \
    --storage.tsdb.path /var/lib/prometheus/ \
    --web.console.templates=/etc/prometheus/consoles \
    --web.console.libraries=/etc/prometheus/console_libraries

[Install]
WantedBy=multi-user.target
```

- **Change the ownership of following files and directories to `prometheus` user**

```
sudo chown prometheus:prometheus /etc/prometheus
sudo chown prometheus:prometheus /usr/local/bin/prometheus
sudo chown prometheus:prometheus /usr/local/bin/promtool
sudo chown -R prometheus:prometheus /etc/prometheus/consoles
sudo chown -R prometheus:prometheus /etc/prometheus/console_libraries
sudo chown -R prometheus:prometheus /var/lib/prometheus
```

- **Start the `prometheus service`**

```
sudo systemctl daemon-reload
sudo systemctl enable prometheus
sudo systemctl start prometheus
```

### 1.4 - Access the Prometheus Web UI

- You can now access the Prometheus Dashboard (Web UI ) from the browser with following link: </br></br>
  **<prometheus_server_public_ip_or_dns_name>:9090**
