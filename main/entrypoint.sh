#!/bin/bash

# Function to restart the container
restart_container() {
    # Check if the container is running and stop it
    if [ "$(docker ps -q -f name=my_container_name)" ]; then
        docker-compose down
    fi

    # Rebuild the Docker image
    docker-compose build

    # Start a new Docker container
    docker-compose up -d
}

# Start the file watcher to monitor changes in the backupfiles directory
while inotifywait -r -e modify,move,create,delete /usr/src/main/backupfiles; do
    # Restart the container
    restart_container

    # Run main2.py inside the container after restarting
    docker exec -d my_container_name python3 main2.py
done

