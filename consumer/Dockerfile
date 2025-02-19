FROM python:3.9

WORKDIR /app

COPY app.py .

RUN pip install requests

# Create a directory for storing received data
RUN mkdir /data

# Define a volume for persistent storage
VOLUME /data

CMD ["python", "app.py"]
