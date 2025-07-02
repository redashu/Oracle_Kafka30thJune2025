# steps 

### configure DNS / hostname (all Nodes) for prod ENV 

## Installing java and kafka and setup ENV variable 

```
dnf install java-11*/openjdk-11-java
wget https://dlcdn.apache.org/kafka/3.9.1/kafka_2.13-3.9.1.tgz
tar xvf kafka_2.13-3.9.1.tgz

===>
JAVA_HOME=/usr/lib/jvm/java-11-amazon-corretto.x86_64
KAFKA_HOME=/home/ec2-user/kafka_2.13-3.9.1
PATH=$PATH:$JAVA_HOME/bin:$KAFKA_HOME/bin
export PATH

```

# using Kraft mode -- need server.properties 

### navigate to server.properties file in Kraft mode 

```
[ec2-user@broker3 ~]$ ls
kafka_2.13-3.9.1  kafka_2.13-3.9.1.tgz

[ec2-user@broker3 ~]$ cd  ~/kafka_2.13-3.9.1/

[ec2-user@broker3 kafka_2.13-3.9.1]$ ls
LICENSE  NOTICE  bin  config  libs  licenses  logs  site-docs

[ec2-user@broker3 kafka_2.13-3.9.1]$ cd config/

[ec2-user@broker3 config]$ ls
connect-console-sink.properties    connect-file-source.properties   consumer.properties  server.properties
connect-console-source.properties  connect-log4j.properties         kraft                tools-log4j.properties
connect-distributed.properties     connect-mirror-maker.properties  log4j.properties     trogdor.conf
connect-file-sink.properties       connect-standalone.properties    producer.properties  zookeeper.properties
[ec2-user@broker3 config]$ 
[ec2-user@broker3 config]$ cd  kraft/
[ec2-user@broker3 kraft]$ 
[ec2-user@broker3 kraft]$ ls
broker.properties  controller.properties  reconfig-server.properties  server.properties
[ec2-user@broker3 kraft]$ 


===> changes in server.properties file 


# The role of this server. Setting this puts us in KRaft mode
process.roles=broker,controller  # by default 
# The node id associated with this instance's roles
node.id=3  # Node1 == 1 , node2= 2 , node3 = 3
# The connect string for the controller quorum (same for all node)
controller.quorum.voters=1@172.31.40.73:9093,2@172.31.32.6:9093,3@172.31.47.127:9093
# format - node_id@node_ip:9093

#     listeners = PLAINTEXT://your.host.name:9092
listeners=PLAINTEXT://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093

# If not set, it uses the value for "listeners".
advertised.listeners=PLAINTEXT://172.31.47.127:9092,CONTROLLER://172.31.47.127:9093

# current_nodeIP/hostname/publicIP 

# A comma separated list of directories under which to store log files
log.dirs=/home/ec2-user/.kraft-kafka
```

### generate UUID / cluster-id (any one node)
### use generate UUID / cluster-id in all the nodes for formating purpose 
```
kafka-storage.sh random-uuid
```

### use above id to format storage  (all nodes)

```
kafka-storage.sh   format -t PohmB0c6TMe5XPXKWbOIuw  -c /home/ec2-user/kafka_2.13-3.9.1/config/kraft/server.properties 

===> this will create log.dirs directory with required structure 
```

### star kafka server process  use systemd (in prod env)

### creating systemd file 

```
sudo vi /etc/systemd/system/kafka.service
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

### how to start kafka 

```
 sudo systemctl daemon-reload 
 sudo systemctl start kafka
 sudo systemctl status kafka
 sudo systemctl enable kafka # auto-start after reboot / stop 

 sudo systemctl restart kafka # if you made any changes in configuration of kafka
 ```





