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



