import json
import asyncio
import threading
from fastapi import FastAPI, WebSocket
from kafka import KafkaConsumer

app = FastAPI()

TOPIC = "ashu-aws-oci-events" # change to your topic name
KAFKA_BROKER = '172.31.40.73:9092'  # Or use private IP if needed
GROUP_ID = "ec2-consumer-api" # change some other name 

# Shared queue between Kafka thread and WebSocket
message_queue = asyncio.Queue()

def consume_kafka():
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        group_id=GROUP_ID,
        auto_offset_reset='latest',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )
    for msg in consumer:
        print(f"Consumed: {msg.value}")
        asyncio.run(message_queue.put(msg.value))

# Launch Kafka consumer in background thread
threading.Thread(target=consume_kafka, daemon=True).start()

@app.websocket("/ws/ec2")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            msg = await message_queue.get()
            await websocket.send_json(msg)
    except Exception as e:
        print(f"WebSocket error: {e}")
        await websocket.close()