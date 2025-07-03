# Steps

## Amazon Linux 2023 / Oracle linux 8/9  with (jdk11)

### Installing JDK 11 or Later (All Nodes)

```sh
sudo dnf install java-11-amazon-corretto-devel.x86_64 java-11-amazon-corretto.x86_64 -y
```

#### Checking Java Binary Path

```sh
readlink -f $(which java)
# Output example:
/usr/lib/jvm/java-11-amazon-corretto.x86_64/bin/java
```

### Download Kafka Binary (All Nodes)

```sh
wget https://dlcdn.apache.org/kafka/3.9.1/kafka_2.13-3.9.1.tgz
tar xvf kafka_2.13-3.9.1.tgz
```

### Set Environment Variables in `.bashrc` (All Nodes)

```sh
JAVA_HOME=/usr/lib/jvm/java-11-amazon-corretto.x86_64
KAFKA_HOME=/home/ec2-user/kafka_2.13-3.9.1
PATH=$PATH:$JAVA_HOME/bin:$KAFKA_HOME/bin
export PATH
```

### Change Kafka Storage Location (All Nodes)

Edit the `server.properties` file:

```sh
cd ~/kafka_2.13-3.9.1/config/kraft/
vim server.properties
```

Example configuration:

```properties
log.dirs=/home/ec2-user/.kraft-kafka
process.roles=broker,controller
node.id=1  # Unique per node (1, 2, 3)
controller.quorum.voters=1@<IP_NODE1>:9093,2@<IP_NODE2>:9093,3@<IP_NODE3>:9093
listeners=PLAINTEXT://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093
advertised.listeners=PLAINTEXT://<NODE_PRIVATE_IP>:9092 # you can try EIP
log.dirs=/var/lib/kafka/data
num.partitions=3
default.replication.factor=3
min.insync.replicas=2
```

### Generate KRaft UUID (Only on One Node)

```sh
kafka-storage.sh random-uuid
# Example output:
PohmB0c6TMe5XPXKWbOIuw
```

### Format Storage (All Nodes)

```sh
kafka-storage.sh format -t PohmB0c6TMe5XPXKWbOIuw -c /home/ec2-user/kafka_2.13-3.9.1/config/kraft/server.properties
```

### Create systemd Unit File (All Nodes)

Create `/etc/systemd/system/kafka.service`:

```ini
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

### Start Kafka Service (All Nodes)

```sh
sudo systemctl daemon-reload
sudo systemctl enable kafka
sudo systemctl start kafka
```

## Verify Cluster (All Nodes)

```sh
jps
# Example output:
30839 Jps
30216 Kafka

netstat -nlpt
# Example output:
# (Not all processes could be identified, non-owned process info will not be shown, you would have to be root to see it all.)
# Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -
tcp6       0      0 :::9092                 :::*                    LISTEN      30216/java
tcp6       0      0 :::9093                 :::*                    LISTEN      30216/java
tcp6       0      0 :::37561                :::*                    LISTEN      30216/java
tcp6       0      0 :::22                   :::*                    LISTEN      -
```

## Additional Commands

```sh
kafka-metadata-quorum.sh --bootstrap-server localhost:9092 describe --status
# Example output:
ClusterId:              PohmB0c6TMe5XPXKWbOIuw
LeaderId:               3
LeaderEpoch:            274
HighWatermark:          653
MaxFollowerLag:         0
MaxFollowerLagTimeMs:   89
CurrentVoters:          [{"id": 1, "directoryId": null, "endpoints": ["CONTROLLER://172.31.40.73:9093"]}, {"id": 2, "directoryId": null, "endpoints": ["CONTROLLER://172.31.32.6:9093"]}, {"id": 3, "directoryId": null, "endpoints": ["CONTROLLER://172.31.47.127:9093"]}]
CurrentObservers:       []

kafka-broker-api-versions.sh --bootstrap-server localhost:9092
# Example output:
172.31.47.127:9092 (id: 3 rack: null) -> (
    Produce(0): 0 to 11 [usable: 11],
)
```