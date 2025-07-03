import re
import time
from kafka import KafkaProducer

# Kafka setup
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    client_id='ashu_producer_client',
    value_serializer=lambda v: str(v).encode('utf-8')
)
topic_name = 'web-logs'

# Apache log path
log_file_path = '/var/log/httpd/access_log'

# Regex pattern to extract IP and URI
log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[.*?\] "(GET|POST|HEAD|OPTIONS|PUT|DELETE) (?P<uri>/\S*) HTTP/1\.[01]"'
)

# Start tailing the log
with open(log_file_path, 'r') as file:
#    file.seek(0, 2)  # Move to end of file

    while True:
        line = file.readline()
        if not line:
            time.sleep(0.5)
            continue  # No new line, wait and retry

        match = log_pattern.search(line)
        if match:
            uri = match.group("uri")
            if uri.startswith("/user"):
                ip = match.group("ip")
                msg = f"IP: {ip}, URI: {uri}"
                print(f"Sending: {msg}") #
                producer.send(topic_name, value=msg)

# Cleanup (not reachable unless you wrap in try-finally or break loop)
producer.flush()
producer.close()

