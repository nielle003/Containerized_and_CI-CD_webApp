pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    docker run --rm \
                      -v ${WORKSPACE}:/workspace \
                      -w /workspace \
                      python:3.11-slim \
                      sh -c "pip install --no-cache-dir -r requirements.txt && pytest"
                '''
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t simple-web-app:${BUILD_NUMBER} .'
                sh 'docker tag simple-web-app:${BUILD_NUMBER} simple-web-app:latest'
            }
        }
        
        stage('Test Docker Container') {
            steps {
                sh '''
                    docker run -d -p 8001:8000 --name test-app-${BUILD_NUMBER} simple-web-app:${BUILD_NUMBER}
                    sleep 5
                    curl -f http://172.17.0.1:8001/health || (docker logs test-app-${BUILD_NUMBER} && exit 1)
                    docker stop test-app-${BUILD_NUMBER}
                    docker rm test-app-${BUILD_NUMBER}
                '''
            }
        }
    }
    
    post {
        success {
            echo '✅ Pipeline succeeded! Docker image simple-web-app:${BUILD_NUMBER} is ready.'
        }
        failure {
            echo '❌ Pipeline failed. Check logs above.'
            sh 'docker ps -a | grep test-app || true'
        }
        always {
            sh 'docker system prune -f || true'
        }
    }
}