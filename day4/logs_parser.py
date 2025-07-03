import re
import time

# Apache log path
log_file_path = '/var/log/httpd/access_log'

# Regex pattern to extract IP and URI
log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[.*?\] "(GET|POST|HEAD|OPTIONS|PUT|DELETE) (?P<uri>/\S*) HTTP/1\.[01]"'
)
with open(log_file_path, 'r') as file:
    # file.seek(0, 2)  # REMOVE THIS

    while True:
        line = file.readline()
        if not line:
            break  # Exit after reading the whole file

        match = log_pattern.search(line)
        if match:
            uri = match.group("uri")
            if uri.startswith("/user"):
                ip = match.group("ip")
                msg = f"IP: {ip}, URI: {uri}"
                print(f"Sending: {msg}")
