import requests
import time

# The file to store data (inside Docker volume)
OUTPUT_FILE = "/data/output.txt"

# The producer service can be reached by its service name in Docker Compose
PRODUCER_URL = "http://producer:5000/data"

while True:
    try:
        # Get the data from the producer
        response = requests.get(PRODUCER_URL)
        data = response.text

        # Append the received data to the output file
        with open(OUTPUT_FILE, "a") as f:
            f.write(data + "\n")
        print("Wrote:", data)
    except Exception as e:
        print("Error fetching data:", e)
    
    time.sleep(3)
