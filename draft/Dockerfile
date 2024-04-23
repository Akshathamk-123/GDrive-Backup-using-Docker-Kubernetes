# Use the latest Ubuntu image as the base image
FROM ubuntu:latest

# Update package lists and install Python 3, pip3, and watchdog
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    python3 -m pip install --upgrade pip 

# Set the working directory inside the container
WORKDIR /usr/src/main

# Copy the contents of the app folder on the host into the container's working directory
COPY app/* ./

# Copy the backupfiles directory from the host into the container's working directory
COPY backupfiles /usr/src/main/backupfiles

# Install Python dependencies listed in the requirements.txt file
RUN pip3 install --no-cache-dir -r requirements.txt

# Set the default command to execute when the container starts
CMD ["python3", "main.py"]

