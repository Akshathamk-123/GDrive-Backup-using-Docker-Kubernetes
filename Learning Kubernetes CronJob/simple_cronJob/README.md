# Simple Cron Job in Kubernetes

## Start Kubernetes

```bash
$ minikube start

Build a docker image
$ docker build -t simplejob .

Check the docker images
$ docker images

Run the docker image
$ docker run -it --rm simplejob:latest

##Run the job in kubernetes:

create a cronjob in kubernetes
$ kubectl create cronjob simplejob --image=simplejob --schedule="*/5 * * * *" --dry-run-client -o yaml > job.yaml

open job.yaml
and add the following line under containers section (after the -image line):
imagePullPolicy: If NotPresent

Run the cronjob in kubernetes:
$ kubectl apply -f job.yaml

Get the cronjob:
$ kubectl get cronjobs

Watch cronjobs:
$ kubectl get pods --watch

Get logs of the cronjob:
$ kubectl logs job-name  #replace the job-name from the output of get the cronjob command 

#### reference: https://www.youtube.com/watch?v=PUhqw0laR3A
