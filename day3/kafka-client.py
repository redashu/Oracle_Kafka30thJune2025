from confluent_kafka import Producer

# 1. Configure connection
conf = {'bootstrap.servers': '3.1.143.30:9092'}

# 2. Create producer
producer = Producer(conf)

# 3. Get cluster metadata
metadata = producer.list_topics(timeout=10)

# 4. Print basic info
print("\nBrokers:")
for broker in metadata.brokers.values():
    print(f" - {broker.host}:{broker.port}")


print("\nTopics:")
for topic in metadata.topics.values():
    print(f" - {topic.topic} ({len(topic.partitions)} partitions)")

# 5. Clean up
producer.flush()
