# Cloud_Infrastructure_14848
CMU 14848 Cloud Infrastructure and Design homework

`Docker Folder`

This folder has homework 2 screenshots for 14848 homework_2 

URL for docker image: https://hub.docker.com/repository/docker/varunkathuria/python-helloworld
___

`Sentiment-Analysis`

This folder has screenshots for Mini-Project-1.

Link to demo-video: https://youtu.be/K06V6PhaMyo

URL for docker images - 
- https://hub.docker.com/repository/docker/varunkathuria/sa-frontend
- https://hub.docker.com/repository/docker/varunkathuria/sa-webapp
- https://hub.docker.com/repository/docker/varunkathuria/sa-logic

Steps to run Sentiment Analyser on Google Kubernetes Engine on GCP -
- Build sa-logic ```docker build -f Dockerfile -t $DOCKER_USER_ID/sa-logic .```
- Push sa-logic image to docker hub ```docker push $DOCKER_USER_ID/sa-logic```
- Pull and tag sa-logic image via GCP cloud shell from dockerhub and then push it it GCP container registry.
- Navigate to sa-logic container on GCP. Deploy and expose the service on your cluster.
- Build java webapp project to get jar ```mvn install```
- Change SA_LOGIC_API_URL variable in sa-webapp Dockerfile to the external IP of sa-logic-service on GCP. Use the container port only. 
- Build sa-webapp ```docker build -f Dockerfile -t $DOCKER_USER_ID/sa-webapp .```
- Push sa-webapp image to docker hub ```docker push $DOCKER_USER_ID/sa-webapp```
- Pull and tag sa-webapp image via GCP cloud shell from dockerhub and then push it it GCP container registry.
- Navigate to sa-webapp container on GCP. Deploy and expose the service on your cluster.
- Change the POST URL in App.js of sa-frontend to the external IP of sa-webapp-service on GCP. Use the port 8080 only. 
- Build frontend using ```yarn build```
- Build sa-fronted ```docker build -f Dockerfile -t $DOCKER_USER_ID/sa-frontend .```
- Push sa-frontend image to docker hub ```docker push $DOCKER_USER_ID/sa-frontend```
- Pull and tag sa-frontend image via GCP cloud shell from dockerhub and then push it it GCP container registry.
- Navigate to sa-frontend container on GCP. Deploy and expose the service on your cluster.
- Access the sa-frontend-service and we have a working sentiment analyser deployed on GCP.
___

`NoSQL`

Added code file, data files and screenshots for query and results in the NoSQL folder.

___

`Project Checkpoint - Big Data Toolbox Application`

Added code file, and screenshots for Toolbox GUI and all delployments on GCP in the Course-project-checkpoint folder. There are also some yaml files which I used to test deploymenmts on minikube.

URL for docker images - 
- https://hub.docker.com/repository/docker/varunkathuria/frontend-terminal
- https://hub.docker.com/r/jupyter/minimal-notebook
- https://hub.docker.com/r/bitnami/spark
- https://hub.docker.com/layers/bde2020/hadoop-namenode/2.0.0-hadoop3.1.3-java8/
- https://hub.docker.com/layers/bde2020/hadoop-datanode/2.0.0-hadoop3.2.1-java8/

Steps to deploy images on Google Kubernetes Engine on GCP -

Firstly I created a new project and a new cluster on GCP for this toolbox project.

#### Terminal GUI
  
1. Build terminal-fronted ```docker build -f Dockerfile -t $DOCKER_USER_ID/terminal-frontend .```
2. Push terminal-frontend image to docker hub ```docker push $DOCKER_USER_ID/terminal-frontend```
3. Pull and tag terminal-frontend image via GCP cloud shell from dockerhub and then push it it GCP container registry.
4. Navigate to terminal-frontend container on GCP. Deploy and expose the service on your cluster on post 80.
5. Access the terminal-frontend-service.

#### Jupyter

1. Pull and tag ```docker pull jupyter/minimal-notebook``` image via GCP cloud shell from dockerhub and then push it it GCP container registry.
2. Navigate to minimal-notebook container on GCP. Deploy and expose the loadbalancer service on your cluster on post 8888.
3. Access the jupyter-notebook via the jupyter-service URL.
  
#### Spark

1. Pull and tag ```docker pull bitnami/spark``` image via GCP cloud shell from dockerhub and then push it it GCP container registry.
2. Navigate to bitnami/spark container on GCP. While deploying the spark image, add the env variable SPARK_MODE=master and expose the loadbalancer service on your cluster on post 8080.
3. Access spark via the spark-service URL.
  
#### Hadoop Namenode

1. Pull and tag ```docker pull bde2020/hadoop-namenode:2.0.0-hadoop3.1.3-java8```  image via GCP cloud shell from dockerhub and then push it it GCP container registry.
2. Navigate to bde2020/hadoop-namenode container on GCP. While deploying the namenode image, add all the env variablse in ```hadoop.env``` file. Also set CLUSTER_NAME=mycluster env variable. Expose the loadbalancer service on your cluster on post 9000 and 9870..
3. Access hadooop namenode via the namenode-service URL.

#### Hadoop Datanode

1. Pull and tag ```docker pull bde2020/hadoop-datanode:2.0.0-hadoop3.1.3-java8```  image via GCP cloud shell from dockerhub and then push it it GCP container registry.
2. Navigate to bde2020/hadoop-datanode container on GCP. While deploying the namenode image, add all the env variablse in ```hadoop.env``` file. Also set SERVICE_PRECONDITION=http://namenode-service:9000 env variable. No need to expose this as a service.
3. Access hadooop datanode via the datanodes tab on namenode-service URL.

![alt text](https://github.com/starlordvk/Cloud_Infrastructure_14848/master/Course-project-checkpoint/screenshots/Toolbox-terminal.PNG?raw=true)
___
