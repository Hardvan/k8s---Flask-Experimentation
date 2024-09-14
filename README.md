# Kubernetes & Flask Experimentation

This project demonstrates how to deploy a simple Flask application that displays "Hello, World!" using Kubernetes. It covers the process of creating a Flask app, containerizing it with Docker, and deploying it to a Kubernetes cluster.

## Prerequisites

- Docker installed and configured
- Kubernetes cluster (local or cloud-based)
- kubectl command-line tool installed and configured
- Python 3.9 or later

## Project Structure

```plaintext
kubernetes-flask-hello-world/
├── app.py
├── Dockerfile
├── requirements.txt
└── kubernetes-deployment.yaml
```

## Quick Start

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd kubernetes-flask-hello-world
   ```

2. Build the Docker image:

   ```bash
   docker build -t flask-k8s-hello-world .
   ```

   This command builds a Docker image from your Dockerfile. The `-t` flag tags the image with the name `flask-k8s-hello-world`. The `.` at the end specifies that the Dockerfile is in the current directory.

3. Tag the Docker image:

   ```bash
   docker tag flask-k8s-hello-world your-docker-username/flask-k8s-hello-world
   ```

   This step tags your image with your Docker Hub username, preparing it for pushing to Docker Hub. Replace `your-docker-username` with your actual Docker Hub username.

4. Push the image to Docker Hub:

   ```bash
   docker push your-docker-username/flask-k8s-hello-world
   ```

   This command uploads your Docker image to Docker Hub, making it accessible for your Kubernetes cluster to pull. Ensure you're logged in to Docker Hub (`docker login`) before running this command.

5. Deploy to Kubernetes:

   ```bash
   kubectl apply -f kubernetes-deployment.yaml
   ```

   This command creates or updates the resources defined in your `kubernetes-deployment.yaml` file in your Kubernetes cluster.

   > Note: If already deployed, you can delete the existing deployment and redeploy:
   > Check the status of the pods:
   >
   > ```bash
   >  kubectl get pods
   > ```
   >
   > This shows the current running pods in your cluster.
   > Delete the deployment:
   >
   > ```bash
   > kubectl delete -f kubernetes-deployment.yaml
   > ```
   >
   > This removes the existing deployment and associated resources.
   >
   > Redeploy the application:
   >
   > ```bash
   > kubectl apply -f kubernetes-deployment.yaml
   > ```
   >
   > This creates a fresh deployment with your updated configuration or image.

6. Access the application:

   ```bash
   kubectl port-forward service/flask-hello-world 8080:80
   ```

   This command forwards traffic from your local machine's port 8080 to port 80 of the `flask-hello-world` service in your Kubernetes cluster.

   Open a web browser and navigate to `http://localhost:8080`
   You should now see your Flask application's "Hello, World!" message in your web browser.

## Detailed Setup

### 1. Flask Application

The `app.py` file contains a simple Flask application that returns an HTML header with "Hello, World!".

### 2. Dockerfile

The Dockerfile defines how to build the Docker image for our Flask application.

### 3. Kubernetes Deployment

The `kubernetes-deployment.yaml` file defines both the Deployment and Service for our application.

## Deployment

1. Ensure your Kubernetes cluster is running and kubectl is configured correctly.

2. Apply the Kubernetes configuration:

   ```bash
   kubectl apply -f kubernetes-deployment.yaml
   ```

3. Check the status of your pods:

   ```bash
   kubectl get pods
   ```

4. Check the status of your service:

   ```bash
   kubectl get services flask-hello-world
   ```

## Accessing the Application

Use port forwarding to access the application:

```bash
kubectl port-forward service/flask-hello-world 8080:80
```

Then open a web browser and go to `http://localhost:8080`

## Cleanup

To remove the deployment and service:

```bash
kubectl delete -f kubernetes-deployment.yaml
```

## Troubleshooting

If you encounter issues:

1. Check pod status:

   ```bash
   kubectl get pods
   ```

2. View pod logs:

   ```bash
   kubectl logs <pod-name>
   ```

3. Describe the service:

   ```bash
   kubectl describe service flask-hello-world
   ```
