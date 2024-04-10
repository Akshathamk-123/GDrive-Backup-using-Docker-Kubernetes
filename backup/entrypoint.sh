#!/bin/bash

# Set the interval in seconds for the CronJob to run
CRON_INTERVAL=60

# Name of the Docker container
DOCKER_CONTAINER_NAME="inspiring_antonelli"

# Function to restart the container and run main.py
restart_container() {
    # Check if the container is running and stop it
    if [ "$(docker ps -q -f name=$DOCKER_CONTAINER_NAME)" ]; then
        docker-compose down  # Stops the running container
    fi

    # Rebuild the Docker image
    docker-compose build  # Rebuilds the Docker image based on the Dockerfile

    # Start a new Docker container
    docker-compose up -d  # Starts the Docker container in detached mode
    
    # Wait for the container to start
    sleep 5

    # Run main.py inside the container
    docker-compose exec -d $DOCKER_CONTAINER_NAME python3 main.py
    
    docker push aishwarya166/cc_docker_image:latest                                      
    
    # Sleep for the duration specified in the CronJob schedule
    sleep $CRON_INTERVAL

    # Restart the container after sleeping
    restart_container  # Calls the function to restart the Docker container and run main.py
}

# Sleep for the duration specified in the CronJob schedule
sleep $CRON_INTERVAL

# Restart the container after sleeping
restart_container  # Calls the function to restart the Docker container and run main.py


