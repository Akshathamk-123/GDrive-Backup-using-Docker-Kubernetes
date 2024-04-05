#GDrive Backup using Docker & Kubernetes

Python script main2.py monitors a directory (backupfiles), uploads any newly created, modified, or moved files to Google Drive using the Google Drive API, and there's a Dockerfile to containerize your application. Additionally, Docker Compose to manage the Docker container, a shell script (entrypoint.sh) to restart the container when changes are detected in the backupfiles directory, and Kubernetes manifests for setting up a CronJob to periodically trigger the backup process and Persistent Volume (PV) and Persistent Volume Claim (PVC) for storing backup files persistently.

### Utilizing Kubernets yaml config files to appropirately control  containers

### Learning Goals

1. Understand API's and how you can use API's to manipulate Cloud Resoucres
2. Understand containerization and how you can package your application to run on any system
3. Understand how you can control orchestrate containers  using Kubernetes

### Deliverables

   1. Using Google's API, write a python script to upload the contents of your folder to Gdrive. 
   2. Containerize your application and all required dependencies and build a Docker image.
   3. Now,using Kubernets, Orchestrate(Control) your application to conduct back ups of your chosen folder at fixed intervals.
   
The connectivity between the files is as follows:

    main2.py: Monitors the backupfiles directory and uploads files to Google Drive using the Google Drive API.
    Dockerfile: Defines the environment and dependencies for containerizing the application.
    docker-compose.yaml: Orchestrates the Docker container and mounts the backupfiles directory into the container.
    entrypoint.sh: Monitors changes in the backupfiles directory and restarts the Docker container.
    backup_cronJob.yaml: Defines a CronJob in Kubernetes to periodically trigger the backup process.
    pv.yaml and pvc.yaml: Define a Persistent Volume (PV) and a Persistent Volume Claim (PVC) in Kubernetes to store backup files persistently.
    

How to run:

aishwarya@aishwaryalp:~/Documents/CC_027_052_062_739/main$ docker login

aishwarya@aishwaryalp:~/Documents/CC_027_052_062_739/main$ minikube start

aishwarya@aishwaryalp:~/Documents/CC_027_052_062_739/main$ sudo apt install docker-compose

aishwarya@aishwaryalp:~/Documents/CC_027_052_062_739/main$ docker-compose build

aishwarya@aishwaryalp:~/Documents/CC_027_052_062_739/main$ kubectl cluster-info

aishwarya@aishwaryalp:~/Documents/CC_027_052_062_739/main$ kubectl apply -f pv2.yaml

aishwarya@aishwaryalp:~/Documents/CC_027_052_062_739/main$ kubectl apply -f pvc2.yaml

aishwarya@aishwaryalp:~/Documents/CC_027_052_062_739/main$ kubectl apply -f backup_cronJob2.yaml

aishwarya@aishwaryalp:~/Documents/CC_027_052_062_739/main$ docker build -t aishwarya166/cc_project_backup:latest .
                                                                                                                                    
aishwarya@aishwaryalp:~/Documents/CC_027_052_062_739/main$ docker push aishwarya166/cc_project_backup:latest                                                                                                

aishwarya@aishwaryalp:~/Documents/CC_027_052_062_739/main$ docker-compose up -d

aishwarya@aishwaryalp:~/Documents/CC_027_052_062_739/main$ docker ps

aishwarya@aishwaryalp:~/Documents/CC_027_052_062_739/main$ docker rmi aishwarya166/cc_project_backup:latest
Error response from daemon: conflict: unable to remove repository reference "aishwarya166/cc_project_backup:latest" (must force) - container f7167d1d146e is using its referenced image 3880d358461d

aishwarya@aishwaryalp:~/Documents/CC_027_052_062_739/main$ docker stop f7167d1d146e
docker rm f7167d1d146e
f7167d1d146e
f7167d1d146e

aishwarya@aishwaryalp:~/Documents/CC_027_052_062_739/main$ docker rmi aishwarya166/cc_project_backup:latest
Untagged: aishwarya166/cc_project_backup:latest
Untagged: aishwarya166/cc_project_backup@sha256:f6371576f6e2f35731768454b00f2320bbdb7cdf081de69587fc9abe163993b2
Deleted: sha256:3880d358461d338bf7b5691f0b001c81455f8a31b61231530b191465329f7290

aishwarya@aishwaryalp:~/Documents/CC_027_052_062_739/main$ docker build -t aishwarya166/cc_project_backup:latest .
                                                                                                                    0.0s 
aishwarya@aishwaryalp:~/Documents/CC_027_052_062_739/main$ docker push aishwarya166/cc_project_backup:latest

aishwarya@aishwaryalp:~/Documents/CC_027_052_062_739/main$ docker-compose build

aishwarya@aishwaryalp:~/Documents/CC_027_052_062_739/main$ docker-compose up -d

aishwarya@aishwaryalp:~/Documents/CC_027_052_062_739/main$ docker logs main_app_1

aishwarya@aishwaryalp:~/Documents/CC_027_052_062_739/main$ kubectl get cronjobs

aishwarya@aishwaryalp:~/Documents/CC_027_052_062_739/main$ kubectl get pods --watch

aishwarya@aishwaryalp:~/Documents/CC_027_052_062_739/main$ kubectl logs backup-container-28538795-d4p57

