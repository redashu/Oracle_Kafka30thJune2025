# revision 

### Producer and consumer groups info 

<img src="rev1.png">


### kafka cluster architecture 

<img src="rev2.png">


### Installing httpd sample webapp 

```
sudo dnf install httpd -y 

pc@kafka-instance ~]$ 
[opc@kafka-instance ~]$ cd  /var/www/html/
[opc@kafka-instance html]$ ls
[opc@kafka-instance html]$ echo "hello world from OCI vm" >index.html 
-bash: index.html: Permission denied
[opc@kafka-instance html]$ sudo -s
[root@kafka-instance html]# 
[root@kafka-instance html]# echo "hello world from OCI vm" >index.html
[root@kafka-instance html]# ls
index.html
[root@kafka-instance html]# mkdir user
[root@kafka-instance html]# echo "hello from user URL" >user/index.html
[root@kafka-instance html]# 

 12  systemctl start httpd
   13  systemctl status httpd
   14  curl ifconfig.me 
   15  curl localhost
   16  curl localhost/user
   17  cd /var/log/httpd/
   18  ls


curl localhost/user
   17  cd /var/log/httpd/
   18  ls
   19  cat access_log 
```

### Creating topic to send logs 

```
opc@kafka-instance ~]$ kafka-topics.sh  --bootstrap-server localhost:9092 --list
demo_topic
demotopic
[opc@kafka-instance ~]$ kafka-topics.sh  --bootstrap-server localhost:9092 --create --topic  web-logs
Created topic web-logs.
[opc@kafka-instance ~]$ kafka-topics.sh  --bootstrap-server localhost:9092 --list
demo_topic
demotopic
web-logs

```

## to send logs to kafka topic

```
python3  finalproducer.py

```

### in second terminal 

```
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic web-logs  --from-beginning 
```

### summary of small project i have created 

<img src="project1.png">


### creating python consumer with flask webapp ui to show consumed messages

```
pip3 install flask 
python3 deploy.py 
# it will deploy consumer + webapp (ip:5000)
```