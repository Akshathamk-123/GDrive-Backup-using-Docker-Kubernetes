# Use the latest Ubuntu image as the base image
FROM ubuntu:latest

# Update package lists
RUN apt-get update

# Install Python 3 and pip3
RUN apt-get install -y python3 python3-pip

# Set the working directory inside the container
WORKDIR /usr/src/backup

# Copy the contents of the app folder on the host into the container's working directory
COPY app/* ./

# Copy the backupfiles directory from the host into the container's working directory
COPY backupfiles /usr/src/backup/backupfiles

# Install Python dependencies listed in the requirements.txt file
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the modified entrypoint script into the container
COPY entrypoint.sh /usr/src/backup/entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /usr/src/backup/entrypoint.sh

# Set the default command to execute when the container starts
#CMD ["./entrypoint.sh"]
CMD ["python3", "main.py"]
