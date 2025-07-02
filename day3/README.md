### Revision 

<img src="rev1.png">

### Kafka dataflow 

<img src="rev2.png">

### kafka producer details 

<img src="rev3.png">

### kafka topics 

<img src="rev4.png">

### more on topics 

<img src="rev5.png">

## Kafka multi node cluster understanding 

<img src="cls1.png">

### kafka multi node cluster setup understadning

<img src="cls2.png">

## as kafka client --connecting to broker1

```
kafka-topics.sh  --bootstrap-server 3.1.143.30:9092 --list

kafka-topics.sh  --bootstrap-server 3.1.143.30:9092 --create --topic   oracle-data1  --partitions 3 --replication-factor  2
Created topic oracle-data1.
[ec2-user@broker1 ~]$ 
[ec2-user@broker1 ~]$ 
[ec2-user@broker1 ~]$ kafka-topics.sh  --bootstrap-server 3.1.143.30:9092 --list
oracle-data1
poc-topic1
topic2
[ec2-user@broker1 ~]$ kafka-topics.sh  --bootstrap-server 3.1.143.30:9092 --describe --topic oracle-data1 
Topic: oracle-data1	TopicId: u3lZmULPRB2AmRq6nIJUUQ	PartitionCount: 3	ReplicationFactor: 2	Configs: segment.bytes=1073741824
	Topic: oracle-data1	Partition: 0	Leader: 1	Replicas: 1,2	Isr: 1,2	Elr: 	LastKnownElr: 
	Topic: oracle-data1	Partition: 1	Leader: 2	Replicas: 2,3	Isr: 2,3	Elr: 	LastKnownElr: 
	Topic: oracle-data1	Partition: 2	Leader: 3	Replicas: 3,1	Isr: 3,1	Elr: 	LastKnownElr: 
[ec2-user@broker1 ~]$ 



```
