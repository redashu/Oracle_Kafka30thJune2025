from kafka import  KafkaConsumer,KafkaAdminClient
from kafka.admin import NewTopic

# Initialize a Kafka admin client
admin_client = KafkaAdminClient(
    bootstrap_servers='3.1.143.30:9092',
    client_id='my_admin_client'
)
# Initialize a Kafka consumer without any topic
consumer = KafkaConsumer(
    bootstrap_servers='3.1.143.30:9092');

# fetch the list of topics
topics = consumer.topics()
print("Available topics:", topics)

## list using for loop
for topic in topics:
    print("Topic:", topic)

# Create a new topic
new_topic = NewTopic(name='ashu-python-topic1', num_partitions=1,replication_factor=1)
# Create the topic using the admin client
admin_client.create_topics(new_topics=[new_topic], validate_only=False)


                        