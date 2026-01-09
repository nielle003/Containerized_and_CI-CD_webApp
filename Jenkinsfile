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
                    echo "Cleaning up any existing test containers..."
                    docker rm -f test-app-${BUILD_NUMBER} || true
                    docker ps | grep test-app | awk '{print $1}' | xargs -r docker rm -f || true
                    
                    echo "Starting container..."
                    docker run -d -p 8001:8000 --name test-app-${BUILD_NUMBER} simple-web-app:${BUILD_NUMBER}
                    
                    echo "Waiting for container to start..."
                    sleep 10
                    
                    echo "Container status:"
                    docker ps | grep test-app-${BUILD_NUMBER}
                    
                    echo "Container logs:"
                    docker logs test-app-${BUILD_NUMBER}
                    
                    echo "Testing health endpoint..."
                    for i in 1 2 3 4 5; do
                        if curl -f http://localhost:8001/health; then
                            echo "Health check passed!"
                            break
                        else
                            echo "Attempt $i failed, retrying..."
                            sleep 2
                        fi
                    done
                    
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
            sh 'docker rm -f $(docker ps -aq --filter name=test-app) || true'
            sh 'docker system prune -f || true'
        }
    }
}