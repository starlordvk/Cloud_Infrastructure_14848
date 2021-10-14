# Cloud_Infrastructure_14848
CMU 14848 Cloud Infrastructure and Design homework

`Docker Folder`

This folder has homework 2 screenshots for 14848 homework_2 

URL for docker image: https://hub.docker.com/repository/docker/varunkathuria/python-helloworld
___

`Sentiment-Analysis`

This folder has screenshots for Mini-Project-1.

Link to demo-video: https://drive.google.com/file/d/1AjqGf6_4GneBj3wRpostPFohy5LJNPEn/view?usp=sharing

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

