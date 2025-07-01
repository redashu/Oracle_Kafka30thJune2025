from kafka import KafkaProducer


# Initialize a Kafka producer
producer = KafkaProducer(
    bootstrap_servers='3.1.143.30:9092',
    client_id='ashu_producer_client', # options to identify the producer
    value_serializer=lambda v: str(v).encode('utf-8')  # Serialize messages as UTF-8 strings
)

# Send a message to the 'test' topic
topic_name = 'ashu-python-topic1'
messages = "Hello, Kafka! This is a test message. from ashutoshh"
mydata = producer.send(topic_name, value=messages)
mydata.get(timeout=10)  # Wait for the message to be sent
print(f"Message sent to topic '{topic_name}': {messages}")
# flush the producer to ensure all messages are sent
producer.flush()
# Close the producer
producer.close()
