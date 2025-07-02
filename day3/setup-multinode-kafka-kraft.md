# Steps

## Configure DNS / Hostname (All Nodes) for Production Environment

## Install Java, Kafka, and Set Environment Variables (All Nodes)

```sh
dnf install java-11*/openjdk-11-java
wget https://dlcdn.apache.org/kafka/3.9.1/kafka_2.13-3.9.1.tgz
tar xvf kafka_2.13-3.9.1.tgz

# Set environment variables
JAVA_HOME=/usr/lib/jvm/java-11-amazon-corretto.x86_64
KAFKA_HOME=/home/ec2-user/kafka_2.13-3.9.1
PATH=$PATH:$JAVA_HOME/bin:$KAFKA_HOME/bin
export PATH
```

---

## Using KRaft Mode – Update `server.properties` (All Nodes)

### Navigate to `server.properties` in KRaft Mode

```sh
cd ~/kafka_2.13-3.9.1/config/kraft/
ls
# Output:
# broker.properties  controller.properties  reconfig-server.properties  server.properties
```

### Edit `server.properties`

```properties
# The role of this server. Setting this puts us in KRaft mode
process.roles=broker,controller

# The node id associated with this instance's roles
node.id=3  # Node1 = 1, Node2 = 2, Node3 = 3

# The connect string for the controller quorum (same for all nodes)
controller.quorum.voters=1@172.31.40.73:9093,2@172.31.32.6:9093,3@172.31.47.127:9093
# Format: node_id@node_ip:9093

# Listeners
listeners=PLAINTEXT://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093

# Advertised listeners
advertised.listeners=PLAINTEXT://172.31.47.127:9092,CONTROLLER://172.31.47.127:9093

# Log directories
log.dirs=/home/ec2-user/.kraft-kafka
```

---

## Generate UUID / Cluster ID (Any One Node)

```sh
kafka-storage.sh random-uuid
```

Use the generated UUID/cluster-id on all nodes for formatting.

---

## Format Storage (All Nodes)

```sh
kafka-storage.sh format -t <CLUSTER_ID> -c /home/ec2-user/kafka_2.13-3.9.1/config/kraft/server.properties
# This will create the log.dirs directory with the required structure
```

---

## Start Kafka Server Process Using systemd (Production Environment)

### Create systemd Service File

```ini
# /etc/systemd/system/kafka.service
[Unit]
Description=Apache Kafka (KRaft)
After=network.target

[Service]
User=ec2-user
Group=ec2-user
ExecStart=/home/ec2-user/kafka_2.13-3.9.1/bin/kafka-server-start.sh /home/ec2-user/kafka_2.13-3.9.1/config/kraft/server.properties
Restart=on-failure
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
```

---

## Start Kafka

```sh
sudo systemctl daemon-reload
sudo systemctl start kafka
sudo systemctl status kafka
sudo systemctl enable kafka   # Auto-start after reboot/stop
sudo systemctl restart kafka # If you made any changes to the configuration
```
