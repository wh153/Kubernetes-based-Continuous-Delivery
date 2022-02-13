# Kubernetes-based-Continuous-Delivery

This is a repository for the second project of IDS 721 Clouding computing. 


Using AWS cloud9 as development environment and github as source control, we create a microservice for two calculations utilizing recursion and dynamic programming, which is simialr to project 1.


## Project2 implementation & Workflow
First, An AWS Cloud9 environment supported by EC2 instance is created for this assignment.

Then the calculator is implemented.

A FastAPI is built for providing the micro-service.

A Docker Image is built holding all the dependencies.

The Amazon Elastic Container Registry (Amazon ECR) is used for storing the image.

The service is a Kubernetes based service using ECS and routed on Load Balancer, containing Continuous Delivery.

CI/CD workflow is built in this assignment

 
<img width="1778" alt="ECR" src="https://user-images.githubusercontent.com/89416055/153735659-b96310b5-4137-45c2-a9af-0b447761e42d.png">

<img width="1792" alt="ECS1" src="https://user-images.githubusercontent.com/89416055/153735676-150f3cef-5800-49dd-bfcd-5c54c308361b.png">

<img width="1792" alt="ECS2" src="https://user-images.githubusercontent.com/89416055/153735682-b265bb53-012d-4d92-8b4e-ec459ae07952.png">

<img width="1792" alt="LoadBalancer" src="https://user-images.githubusercontent.com/89416055/153735688-36501ba9-4cd4-409f-991f-a1c650b2febb.png">
