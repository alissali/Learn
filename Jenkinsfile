pipeline {
    agent any

    environment {
        // You can define any global environment variables here
        DOCKER_IMAGE = "my-python-app"
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from GitHub repository
                git 'https://github.com/yourusername/your-python-repo.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                // Set up a Python virtual environment
                sh 'python3 -m venv venv'  // Create virtual environment
                sh './venv/bin/pip install -r requirements.txt'  // Install dependencies
            }
        }

        stage('Test') {
            steps {
                // Run tests using pytest (or your preferred test framework)
                sh './venv/bin/pytest tests/'  // Make sure your tests are in a 'tests/' folder
            }
        }

        stage('Docker Build') {
            steps {
                // Build the Docker image
                sh 'docker build -t $DOCKER_IMAGE .'  // Dockerize your app
            }
        }

        stage('Docker Push') {
            steps {
                withCredentials([string(credentialsId: 'docker-hub-token', variable: 'DOCKER_TOKEN')]) {
                    // Login to Docker Hub
                    sh 'docker login -u myusername -p $DOCKER_TOKEN'
                    // Push the Docker image to Docker Hub or any other registry
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }

        stage('Deploy') {
            steps {
                // Deploy the container, this example is for Docker on local or cloud
                sh 'docker run -d -p 80:80 $DOCKER_IMAGE'  // Run container on port 80
            }
        }
    }
}

