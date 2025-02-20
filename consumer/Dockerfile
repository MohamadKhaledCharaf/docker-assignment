# Use  Python 3.9 image as the base image
FROM python:3.9
# Set the working directory inside the container to /app
WORKDIR /app
# Copy the application script (app.py) from your local directory into the container's /app directory
COPY app.py .
# Install the 'requests' library required by the application
RUN pip install requests
# Create a directory for storing received data
RUN mkdir /data
# Define a volume for persistent storage
VOLUME /data
CMD ["python", "app.py"]
