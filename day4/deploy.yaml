from flask import Flask, render_template_string
from kafka import KafkaConsumer
import threading

# Kafka config
KAFKA_TOPIC = 'web-logs'
KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092'

# In-memory list to store logs
log_data = []

# HTML template (inline for simplicity)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Live /user Logs</title>
    <meta http-equiv="refresh" content="5">
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        pre { background: #f4f4f4; padding: 10px; white-space: pre-wrap; }
    </style>
</head>
<body>
    <h2>Live Kafka Logs for /user URIs (Auto-refresh every 5s)</h2>
    <pre>
{% for entry in logs %}
{{ entry }}
{% endfor %}
    </pre>
</body>
</html>
"""

# Start Flask app
app = Flask(__name__)

@app.route("/")
def show_logs():
    # Show last 50 log entries
    return render_template_string(html_template, logs=log_data[-50:])

# Kafka consumer thread
def consume_logs():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        auto_offset_reset='latest',
        group_id='log-consumer-group',
        enable_auto_commit=True,
        value_deserializer=lambda x: x.decode('utf-8')
    )

    for message in consumer:
        log_data.append(message.value)
        print(f"Consumed: {message.value}")

# Start Kafka consumer in background thread
consumer_thread = threading.Thread(target=consume_logs, daemon=True)
consumer_thread.start()

# Run the Flask web app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)