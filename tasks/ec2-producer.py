import boto3
import json
from kafka import KafkaProducer
import time

# Set your AWS region
REGION = 'ap-south-1'
KAFKA_BROKER = '172.31.40.73:9092'  # Or use private IP if needed
topic_name = 'ashu-aws-oci-events' # please change to your topic name
# Initialize EC2 client
ec2 = boto3.client('ec2', region_name=REGION)

# Kafka producer setup
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def get_instance_name(tags):
    if tags:
        for tag in tags:
            if tag['Key'] == 'Name':
                return tag['Value']
    return "Unnamed"

def fetch_and_send_events():
    print("Fetching EC2 instance states and sending to Kafka...")
    reservations = ec2.describe_instances().get('Reservations', [])
    for res in reservations:
        for instance in res['Instances']:
            name = get_instance_name(instance.get("Tags", []))
            msg = {
                "instance_id": instance["InstanceId"],
                "name": name,
                "state": instance["State"]["Name"],
                "timestamp": instance["LaunchTime"].isoformat(),
                "region": REGION
            }
            producer.send(topic_name, value=msg)
            print(f"Published: {msg}")

if __name__ == "__main__":
    while True:
        fetch_and_send_events()
        time.sleep(10)
