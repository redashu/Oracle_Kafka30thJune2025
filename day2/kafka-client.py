from kafka import KafkaProducer, KafkaConsumer
# Initialize a Kafka consumer without any topic
consumer = KafkaConsumer(
    bootstrap_servers='3.1.143.30:9092');

# fetch the list of topics
topics = consumer.topics()
print("Available topics:", topics)

## list using for loop
for topic in topics:
    print("Topic:", topic)