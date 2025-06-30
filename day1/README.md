# Oracle_Kafka30thJune2025

### Understanding sending data from sources to target -- problem 

<img src="prob1.png">


### Introduction to distributed messaging and event store platform 

<img src="kafka1.png">

## few more info about apache kafka

<img src="kafka2.png">

### kafka setup for vertical vs horizontal scaling 

<img src="kafka3.png">


### Kafka components and names

<img src="kafka4.png">

### setup kafka options 

<img src="kafka5.png">

# setup apache kafka on any linux based platform

### Prerequisite 

<img src="pre.png">


### basic details to check 

```
[opc@instance-20250630-0613 ~]$ uname -r
5.15.0-309.180.4.el8uek.x86_64

[opc@instance-20250630-0613 ~]$ cat  /etc/os-release 
NAME="Oracle Linux Server"
VERSION="8.10"
ID="ol"
ID_LIKE="fedora"
VARIANT="Server"
VARIANT_ID="server"
VERSION_ID="8.10"

```

## setup Java 11 with devel support 

### Installation of jdk 11

```

```

### verify and set java_home env variable 

```
ec2-user@ip-172-31-40-73 ~]$ java -version 
openjdk version "11.0.27" 2025-04-15 LTS

OpenJDK Runtime Environment Corretto-11.0.27.6.1 (build 11.0.27+6-LTS)
OpenJDK 64-Bit Server VM Corretto-11.0.27.6.1 (build 11.0.27+6-LTS, mixed mode)

[ec2-user@ip-172-31-40-73 ~]$ jps
27534 Jps

===> setting ENV 
readlink  -f $(which java)

/usr/lib/jvm/java-11-amazon-corretto.x86_64/bin/java

===> in .bashrc file 
JAVA_HOME=/usr/lib/jvm/java-11-amazon-corretto.x86_64
PATH=$PATH:$JAVA_HOME/bin
export PATH

===>
source ~/.bashrc 

==
echo $JAVA_HOME
/usr/lib/jvm/java-11-amazon-corretto.x86_64

java -version 
jps

```

## kafka version understanding 

<img src="kv.png">

### few basic points to understand in kafka about zookeeper

<img src="zoo.png">

### zookeeper with kafka  

<img src="zoo1.png">


## setup 

### Download kafka 3.9 with scala 2.3 support binary 

```
wget  https://dlcdn.apache.org/kafka/3.9.1/kafka_2.13-3.9.1.tgz

[ec2-user@ip-172-31-40-73 ~]$ ls
kafka_2.13-3.9.1.tgz

[ec2-user@ip-172-31-40-73 ~]$ tar  xvf  kafka_2.13-3.9.1.tgz 
kafka_2.13-3.9.1/
kafka_2.13-3.9.1/LICENSE
kafka_2.13-3.9.1/NOTICE

===>
[ec2-user@ip-172-31-40-73 ~]$ ls  kafka_2.13-3.9.1
LICENSE  NOTICE  bin  config  libs  licenses  site-docs
[ec2-user@ip-172-31-40-73 ~]$ 
[ec2-user@ip-172-31-40-73 ~]$ ls  kafka_2.13-3.9.1/config/
connect-console-sink.properties    connect-file-source.properties   consumer.properties  server.properties
connect-console-source.properties  connect-log4j.properties         kraft                tools-log4j.properties
connect-distributed.properties     connect-mirror-maker.properties  log4j.properties     trogdor.conf
connect-file-sink.properties       connect-standalone.properties    producer.properties  zookeeper.properties
[ec2-user@ip-172-31-40-73 ~]$ 
[ec2-user@ip-172-31-40-73 ~]$ ls  kafka_2.13-3.9.1/bin/
connect-distributed.sh        kafka-consumer-groups.sh     kafka-metadata-quorum.sh            kafka-topics.sh
connect-mirror-maker.sh       kafka-consumer-perf-test.sh  kafka-metadata-shell.sh             kafka-transactions.sh
connect-plugin-path.sh        kafka-delegation-tokens.sh   kafka-mirror-maker.sh               kafka-verifiable-consumer.sh
connect-standalone.sh         kafka-delete-records.sh      kafka-producer-perf-test.sh         kafka-verifiable-producer.sh
kafka-acls.sh                 kafka-dump-log.sh            kafka-reassign-partitions.sh        trogdor.sh
kafka-broker-api-versions.sh  kafka-e2e-latency.sh         kafka-replica-verification.sh       windows

```

### setting kafka_home variable 

```
[ec2-user@ip-172-31-40-73 ~]$ tail -7  ~/.bashrc 
fi

unset rc
JAVA_HOME=/usr/lib/jvm/java-11-amazon-corretto.x86_64
KAFKA_HOME=/home/ec2-user/kafka_2.13-3.9.1
PATH=$PATH:$JAVA_HOME/bin:$KAFKA_HOME/bin
export PATH


[ec2-user@ip-172-31-40-73 ~]$ 
[ec2-user@ip-172-31-40-73 ~]$ source ~/.bashrc 
[ec2-user@ip-172-31-40-73 ~]$ 


[ec2-user@ip-172-31-40-73 ~]$ kafka-
kafka-acls.sh                       kafka-dump-log.sh                   kafka-reassign-partitions.sh
kafka-broker-api-versions.sh        kafka-e2e-latency.sh                kafka-replica-verification.sh
kafka-client-metrics.sh             kafka-features.sh                   kafka-run-class.sh
kafka-cluster.sh                    kafka-get-offsets.s

```

### starting zookeeper server 

```
zookeeper-server-start.sh  -daemon  /home/ec2-user/kafka_2.13-3.9.1/config/zookeeper.properties 

[ec2-user@ip-172-31-40-73 ~]$ 
[ec2-user@ip-172-31-40-73 ~]$ netstat -nlpt
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::2181                 :::*                    LISTEN      31484/java          
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
tcp6       0      0 :::37265                :::*                    LISTEN      31484/java          
[ec2-user@ip-172-31-40-73 ~]$ 


```

### start apache kafka server 

```
[ec2-user@ip-172-31-40-73 ~]$ kafka-server-start.sh  -daemon /home/ec2-user/kafka_2.13-3.9.1/config/server.properties 
[ec2-user@ip-172-31-40-73 ~]$ 
[ec2-user@ip-172-31-40-73 ~]$ 
[ec2-user@ip-172-31-40-73 ~]$ 
[ec2-user@ip-172-31-40-73 ~]$ jps
31970 QuorumPeerMain
32777 Jps
32701 Kafka


[ec2-user@ip-172-31-40-73 ~]$ netstat -nlpt
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::34985                :::*                    LISTEN      32701/java          
tcp6       0      0 :::2181                 :::*                    LISTEN      31970/java          
tcp6       0      0 :::32963                :::*                    LISTEN      31970/java          
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
tcp6       0      0 :::9092                 :::*                    LISTEN      32701/java          
[ec2-user@ip-172-31-40-73 ~]$ 



```

## Any Producer Can Send Data to a Broker

- **Brokers** have *topics* where message streams are stored.
- A *message/data stream* is a sequence of messages or data.
- A *topic* is similar to a database table (but without constraints).
- You cannot query topics directly; only consumers/subscribers can read data from a topic.

## Topic and Partition Concepts

![Topic and Partition Concepts](tp1.png)

### Kafka clients are producer and consumers

<img src="kclien.png">


### verify can we connect to zookeeper or not 

```
[ec2-user@ip-172-31-40-73 ~]$ zookeeper-shell.sh  localhost:2181 
Connecting to localhost:2181
Welcome to ZooKeeper!
JLine support is disabled

WATCHER::

WatchedEvent state:SyncConnected type:None path:null
ls /
[admin, brokers, cluster, config, consumers, controller, controller_epoch, feature, isr_change_notification, latest_producer_id_block, log_dir_event_notification, zookeeper]
ls /config
[brokers, changes, clients, ips, topics, users]
ls /zookeeper
[config, quota]
ls /zookeeper/config
[]
get  /zookeeper/config

ls /config/brokers
[]
get /config/brokers
null
^C[ec2-user@ip-172-31-40-73 ~]$ ^C

```

## Some zookeeper administrative things to check for kafka better health

###  4-Letter words (4LW)

## checking basic health of zookeeper 

### enable / whitelist 4lw commands 

```
vim /home/ec2-user/kafka_2.13-3.9.1/config/zookeeper.properties
# last line 
4lw.commands.whitelist=*


===>
 zookeeper-server-stop.sh

 ===>
  zookeeper-server-start.sh  -daemon  /home/ec2-user/kafka_2.13-3.9.1/config/zookeeper.properties
```
### lets try again to check 

```

echo "ruok"  | nc localhost 2181 

imok

===>
echo "stat"  | nc localhost 21812181
Zookeeper version: 3.8.4-9316c2a7a97e1666d8f4593f34dd6fc36ecc436c, built on 2024-02-12 22:16 UTC
Clients:
 /127.0.0.1:32924[1](queued=0,recved=31,sent=31)
 /127.0.0.1:52780[0](queued=0,recved=1,sent=0)

Latency min/avg/max: 0/0.4333/4
Received: 36
Sent: 37
Connections: 2
Outstanding: 0
Zxid: 0x23
Mode: standalone
Node count: 28

===>
 93  echo "ruok"  | nc localhost 2181 
   94  echo "stat"  | nc localhost 2181
   95  echo "conf"  | nc localhost 2181
   96  echo "srvr"  | nc localhost 2181
 echo "mntr"  | nc localhost 2181 

 ```
 