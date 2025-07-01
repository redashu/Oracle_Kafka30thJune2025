from kafka import  KafkaConsumer
# Initialize a Kafka consumer
consumer = KafkaConsumer(
    'ashu-python-topic1',  # Specify the topic to consume from
    bootstrap_servers='3.1.143.30:9092',
    client_id='ashu_consumer_client',  # Options to identify the consumer
    auto_offset_reset='earliest',  # Start reading from the earliest message
    #enable_auto_commit=True,  # Automatically commit offsets
    value_deserializer=lambda x: x.decode('utf-8')  # Deserialize messages as
)

# Consume messages from the topic
for message in consumer:
    print(f"Received message: {message.value} from topic: {message.topic} at offset: {message.offset}")