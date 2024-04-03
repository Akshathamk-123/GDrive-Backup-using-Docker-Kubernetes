FROM ubuntu:latest 

# Install necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Set working directory
WORKDIR /usr/src/main

# Copy the contents of the app folder to the container
COPY app/* ./

# Copy the backupfiles directory into the container
COPY backupfiles /usr/src/main/backupfiles

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Set entrypoint
CMD ["python3", "main.py"]

