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





