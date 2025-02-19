# Use a lightweight Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY app.py .

# Install necessary Python libraries
RUN pip install flask

# Expose a port for communication
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]
