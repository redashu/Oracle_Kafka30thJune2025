# Oracle_Kafka30thJune2025

### revision  

<img src="rev1.png">

### verify and started kafka lab environment 

```
[ec2-user@ip-172-31-40-73 ~]$ ls
kafka_2.13-3.9.1  kafka_2.13-3.9.1.tgz
[ec2-user@ip-172-31-40-73 ~]$ echo $JAVA_HOME
/usr/lib/jvm/java-11-amazon-corretto.x86_64
[ec2-user@ip-172-31-40-73 ~]$ echo $KAFKA_HOME
/home/ec2-user/kafka_2.13-3.9.1
[ec2-user@ip-172-31-40-73 ~]$ jps
2330 Jps
[ec2-user@ip-172-31-40-73 ~]$ zookeeper-server-start.sh  -daemon  /home/ec2-user/kafka_2.13-3.9.1/config/zookeeper.properties 
[ec2-user@ip-172-31-40-73 ~]$ jps
2834 Jps
2806 QuorumPeerMain
[ec2-user@ip-172-31-40-73 ~]$ netstat -nlpt
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::36813                :::*                    LISTEN      2806/java           
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
tcp6       0      0 :::2181                 :::*                    LISTEN      2806/java           
[ec2-user@ip-172-31-40-73 ~]$ kafka-server-start.sh  -daemon  /home/ec2-user/kafka_2.13-3.9.1/config/server.properties 
[ec2-user@ip-172-31-40-73 ~]$ jps
3253 Kafka
2806 QuorumPeerMain
3293 Jps
[ec2-user@ip-172-31-40-73 ~]$ netstat -nlpt
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::46511                :::*                    LISTEN      3253/java           
tcp6       0      0 :::36813                :::*                    LISTEN      2806/java           
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
tcp6       0      0 :::2181                 :::*                    LISTEN      2806/java           
tcp6       0      0 :::9092                 :::*                    LISTEN      3253/java           

```

### connecting to remote zookeeper and kafka 

```
echo dump | nc 54.179.159.70  2181 
[ec2-user@ip-172-31-40-73 ~]$ kafka-topics.sh  --bootstrap-server  54.179.159.70:9092  --list 

[ec2-user@ip-172-31-40-73 ~]$ kafka-topics.sh  --bootstrap-server  54.179.159.70:9092  --create --topic ashu-topic1  
Created topic ashu-topic1.
[ec2-user@ip-172-31-40-73 ~]$ kafka-topics.sh  --bootstrap-server  54.179.159.70:9092  --list 
ashu-topic1
[ec2-user@ip-172-31-40-73 ~]$ 

```

