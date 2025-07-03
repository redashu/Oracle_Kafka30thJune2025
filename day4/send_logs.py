from kafka import KafkaProducer


# Initialize a Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    client_id='ashu_producer_client', # options to identify the producer
    value_serializer=lambda v: str(v).encode('utf-8')  # Serialize messages as UTF-8 strings
)

# Send a message to the 'test' topic
topic_name = 'web-logs'
messages = "Hello, Kafka! httpd logs demo"
mydata = producer.send(topic_name, value=messages)
mydata.get(timeout=10)  # Wait for the message to be sent
print(f"Message sent to topic '{topic_name}': {messages}")
# flush the producer to ensure all messages are sent
producer.flush()
# Close the producer
producer.close()
