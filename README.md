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

4. Run the application:
python app.py

5. The API will be running at http://127.0.0.1:8000

Use test-api.http to test the REST API using the REST Client extension in Visual Studio Code.

### API Endpoints
1. GET /: Root endpoint with a welcome message.

2. GET /health: Health check endpoint to confirm the service is running.

3. GET /staff: Retrieve all staff members.

4. GET /staff/<id>: Retrieve a specific staff member by ID.

5. POST /staff: Add a new staff member.

6. PUT /staff/<id>: Update an existing staff member.

7. DELETE /staff/<id>: Delete a staff member.

## Docker Image

The staff-service is containerized using Docker. You can pull the image from Docker Hub:

```bash
docker pull klamichhane738/bestbuy-staff-service:latest
```
## Image link : https://hub.docker.com/repository/docker/klamichhane738/bestbuy-staff-service/general

### Deploying to Kubernetes

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
az aks create --resource-group bestbuy-resource-group --name bestbuy-aks-cluster --node-count 1 --generate-ssh-keys
```

### Connect to the Cluster
```bash
az aks get-credentials --resource-group bestbuy-resource-group --name bestbuy-aks-cluster
```

---

## Step 2: Write the Kubernetes Deployment YAML File

Create a file named `staff-service-deployment.yaml` in the root of your project with the following content:

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

## Step 3: Deploy the Service to AKS

### Apply the Deployment
```bash
kubectl apply -f staff-service-deployment.yaml
```

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


