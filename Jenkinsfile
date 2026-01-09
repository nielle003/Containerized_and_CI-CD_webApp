pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'ls -la'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh '''
                    echo "Building Docker image..."
                    docker build -t simple-web-app:${BUILD_NUMBER} .
                    docker tag simple-web-app:${BUILD_NUMBER} simple-web-app:latest
                '''
            }
        }
        
        stage('Run Container Test') {
            steps {
                sh '''
                    echo "Starting container..."
                    docker run -d -p 8001:8000 --name test-app-${BUILD_NUMBER} simple-web-app:${BUILD_NUMBER}
                    sleep 5
                    echo "Testing health endpoint..."
                    curl -f http://localhost:8001/health
                    echo "Container logs:"
                    docker logs test-app-${BUILD_NUMBER}
                    echo "Stopping container..."
                    docker stop test-app-${BUILD_NUMBER}
                    docker rm test-app-${BUILD_NUMBER}
                '''
            }
        }
        
        stage('List Images') {
            steps {
                sh 'docker images | grep simple-web-app'
            }
        }
    }
    
    post {
        success {
            echo '✅ Build #${BUILD_NUMBER} succeeded! Image created: simple-web-app:${BUILD_NUMBER}'
        }
        failure {
            echo '❌ Build #${BUILD_NUMBER} failed.'
        }
        always {
            sh 'docker system prune -f || true'
        }
    }
}