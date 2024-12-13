# Flask REST API for Staff Management

This project demonstrates a REST API built with Python's Flask framework. The API performs CRUD (Create, Read, Update, Delete) operations on staff data, which can be tested locally and deployed to Azure App Service for cloud hosting.

## Features

- **Retrieve all staff members**: Get a list of all staff.
- **Retrieve a specific staff member by ID**: Fetch details of a staff member by their unique ID.
- **Create a new staff member**: Add a new staff record.
- **Update an existing staff member**: Modify details of an existing staff member by ID.
- **Delete a staff member**: Remove a staff record by ID.

## Prerequisites

Before you can run or deploy this app, ensure you have the following installed:

- **Python 3.x**
- **pip** (Python package manager)
- **Flask** (Install using `pip install Flask`)
- **gunicorn** (Install using `pip install gunicorn`)
- **Azure CLI** (optional, for deployment to Azure)

## Project Structure

- **app.py**: Main Flask application for handling API requests.
- **requirements.txt**: List of Python dependencies needed for the project.
- **test-api.http**: File for testing the REST API endpoints using the REST Client extension in Visual Studio Code.
- **README.md**: Documentation for the project.

## Running Locally

To run the Flask API on your local machine:

1. Clone this repository:

   ```bash
   git clone https://github.com/<your-username>/bestbuy-staff-service.git
2. Navigate to the project directory:
```bash
cd bestbuy-staff-service
```
3. Install the dependencies:

pip install -r requirements.txt

![alt text](<Screenshots/Screenshot (2723).png>)

4. Run the application:
python app.py

![alt text](<Screenshots/Screenshot (2722).png>)

5. The API will be running at http://127.0.0.1:8000

Use test-api.http to test the REST API using the REST Client extension in Visual Studio Code.

![alt text](<Screenshots/Screenshot (2720).png>)

### API Endpoints
1. GET /: Root endpoint with a welcome message.

2. GET /health: Health check endpoint to confirm the service is running.

3. GET /staff: Retrieve all staff members.

4. GET /staff/<id>: Retrieve a specific staff member by ID.

5. POST /staff: Add a new staff member.

6. PUT /staff/<id>: Update an existing staff member.

7. DELETE /staff/<id>: Delete a staff member.

Example of one crud operation: Adding staff:

![alt text](<Screenshots/Screenshot (2726).png>)

## Docker Image

### Build the docker image

```bash
docker build -t klamichhane738/bestbuy-staff-service:latest .
```
### Push to the docker hub
```bash
docker login
docker push klamichhane738/bestbuy-staff-service:latest
```

![alt text](<Screenshots/Screenshot (2744).png>)


The staff-service is containerized using Docker. You can pull the image from Docker Hub:

```bash
docker pull klamichhane738/bestbuy-staff-service:latest
```
## Image link : https://hub.docker.com/repository/docker/klamichhane738/bestbuy-staff-service/general



## Deploying to Kubernetes

## Step 1: Create an AKS Cluster

### Log in to Azure CLI
```bash
az login
```

### Create a Resource Group
```bash
az group create --name bestbuy-resource-group --location eastus
```

### Create an AKS Cluster
```bash
az aks create --resource-group Finalexam --name bestbuy-aks-cluster --node-count 1 --generate-ssh-keys
```

### Connect to the Cluster
```bash
az aks get-credentials --resource-group Finalexam --name bestbuycluster
```

---

![alt text](<Screenshots/Screenshot (2733).png>)

## Step 2: Write the Kubernetes Deployment YAML File

Create a file named `staff-service.yaml` in the root of your project with the following content:

![alt text](<Screenshots/Screenshot (2735).png>)

### `deployment.yaml`:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: staff-service-deployment
  labels:
    app: staff-service
spec:
  replicas: 1
  selector:
    matchLabels:
      app: staff-service
  template:
    metadata:
      labels:
        app: staff-service
    spec:
      containers:
      - name: staff-service-container
        image: klamichhane738/bestbuy-staff-service:latest
        ports:
        - containerPort: 8000
---
apiVersion: v1
kind: Service
metadata:
  name: staff-service
spec:
  selector:
    app: staff-service
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8000
  type: LoadBalancer
```

---

### Step 3: Deploy the Service to AKS

### Apply the Deployment
```bash
kubectl apply -f staff-service.yaml
```
![alt text](<Screenshots/Screenshot (2736).png>)

### Verify the Deployment

#### Check the Pods
```bash
kubectl get pods
```

#### Check the Service
```bash
kubectl get svc
```

Once the service is running, note the `EXTERNAL-IP` of the LoadBalancer to access the `staff-service` API.

---

## Step 4: Push the YAML File to the Repository

### Push YAML File to Git Repository
```bash
git add deployment.yaml
git commit -m "Adding AKS deployment file"
git push origin main
```
# GitHub Actions CI/CD Workflow for BestBuy Staff Service

## Step 1: Fork the Repository and Set Up Secrets

### Fork the Repository
1. Fork the repository: **BestBuy Staff Service**.

### Set Up Secrets
1. Navigate to **Settings > Secrets and variables > Actions** in your forked repository.
2. Add the following Secrets:
   - **DOCKER_USERNAME**: Your Docker Hub username.
   - **DOCKER_PASSWORD**: Your Docker Hub password.
   - **KUBE_CONFIG_DATA**: Your base64-encoded Kubernetes configuration file.
   
   To generate it, run the following command in your terminal:
   ```bash
   cat ~/.kube/config | base64 -w 0 > kube_config_base64.txt
   ```
   Copy the content of `kube_config_base64.txt` into the **KUBE_CONFIG_DATA** secret.

![alt text](<Screenshots/Screenshot (2739).png>)

### Set Up Environment Variables
1. Navigate to **Settings > Secrets and variables > Actions** in your forked repository.
2. Add the following Repository Variables:
   - **DOCKER_IMAGE_NAME**: For example, `bestbuy-staff-service`.
   - **DEPLOYMENT_NAME**: The Kubernetes deployment name. For example, `staff-service-deployment`.
   - **CONTAINER_NAME**: The container name. For example, `staff-service`.

---

## Step 2: Create the Workflow File

### Create the Workflow Directory
1. In the root of your forked repository, create the `.github/workflows/` directory.

### Add the Workflow File
1. Copy the `ci_cd.yaml` file from the **Workflow Files** folder (provided in the original repository) into `.github/workflows/` in your forked repository.

---

## Step 3: Understand the Workflow File

The `ci_cd.yaml` file automates the CI/CD pipeline. Key components include:

### Triggers
The workflow runs whenever a push is made to the `main` branch:
```yaml
on:
  push:
    branches:
      - main
```

### Jobs
1. **Build**: Builds a Docker image for the service and pushes it to Docker Hub.
2. **Test**: Runs automated tests for the application.
3. **Release**: Promotes the Docker image to the latest tag.
4. **Deploy**: Deploys the updated image to AKS using `kubectl`.

### Secrets and Environment Variables
- **Secrets**: (`DOCKER_USERNAME`, `DOCKER_PASSWORD`, `KUBE_CONFIG_DATA`) are securely passed to the workflow.
- **Environment Variables**: (`DOCKER_IMAGE_NAME`, `DEPLOYMENT_NAME`, `CONTAINER_NAME`) are used to parameterize the workflow.

---

## Step 4: Deploy the Application

### Set Up an AKS Cluster
1. Ensure you have a running Azure Kubernetes Service (AKS) cluster.
2. Connect your local machine to the cluster:
   ```bash
   az aks get-credentials --resource-group <resource-group> --name <cluster-name>
   ```

### Deploy BestBuy Staff Service
1. Use the provided deployment file in the **Deployment Files** folder to deploy the service:
   ```bash
   kubectl apply -f staff-service.yaml
   ```

### Push Code Changes
1. Make any code changes in your repository and push them to the `main` branch to trigger the workflow.

### Monitor Workflow Execution
1. Go to the **Actions** tab in your repository to monitor workflow execution (Build, Test, Release, Deploy).

![alt text](<Screenshots/Screenshot (2741).png>)

### Validate the Deployment
1. After the workflow completes, validate that the application is running in the AKS cluster:
   ```bash
   kubectl get pods
   kubectl get services
   ```


![alt text](<Screenshots/Screenshot (2742).png>)

![alt text](<Screenshots/Screenshot (2743).png>)

