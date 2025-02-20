## Components

### Producer
- **Purpose:**  
  The **Data Producer** container runs a simple HTTP server using Python’s built-in libraries. It generates a random number on each request.
- **Files:**  
  - `producer/app.py`: Contains the code to start the HTTP server and return a random number.
  - `producer/Dockerfile`: Defines the base image, copies the application code, installs dependencies, and exposes port `5000`.

### Consumer
- **Purpose:**  
  The **Data Consumer** container periodically requests data from the Producer and writes the received data to a file. This file is stored in a Docker volume, ensuring data persistence.
- **Files:**  
  - `consumer/app.py`: Contains the code to fetch data from the Producer and append it to a file.
  - `consumer/Dockerfile`: Defines the base image, copies the consumer script, sets up a directory for persistent storage, and declares a volume for data persistence.

### Docker Compose
- **Purpose:**  
  The `docker-compose.yml` file orchestrates both the Producer and Consumer containers by:
  - Building the images from their respective Dockerfiles.
  - Setting up a custom Docker network so the containers can communicate using their service names.
  - Creating a Docker volume to persist the data written by the Consumer.
- **Configuration:**  
  - **Services:**
    - `producer`: Builds from `./producer` and exposes port `5000`.
    - `consumer`: Builds from `./consumer` and mounts a volume to persist data at `/data`.
  - **Networks:** A custom network named `app_network` connects the services.
  - **Volumes:** A volume named `data_volume` is used by the Consumer.

---

## How to Build and Run the Project

### Prerequisites
- **Docker:** Ensure Docker is installed on your machine.
- **Docker Compose:** Ensure Docker Compose is installed.

### Building the Images
In the root directory of the repository, run:
```bash
docker-compose build
```
## Running the Containers
After building the images, start the containers by running:
```bash
docker-compose up -d
```
## Verifying the Setup

### Check the Producer
Open a browser or use `curl` to access `http://localhost:5000/` and see the random number generated.

### Check the Consumer Logs
View the logs to verify data is being fetched and stored:
```bash
docker-compose logs consumer
```
## Verify Persistent Storage
The data is saved in a Docker volume (`data_volume`). To inspect the contents of the volume, run:
```bash
docker volume ls
docker run --rm -it -v <volume_name>:/data alpine ls /data
```
## Stopping and Cleaning Up
To stop and remove the containers, network, and volume, run:
```bash
docker-compose down
```
