pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '''
                    docker run --rm -v ${WORKSPACE}:/app -w /app python:3.11-slim pip install --no-cache-dir -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    docker run --rm -v ${WORKSPACE}:/app -w /app python:3.11-slim sh -c "pip install -r requirements.txt && pytest"
                '''
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t simple-web-app:${BUILD_NUMBER} .'
            }
        }
        
        stage('Test Docker Container') {
            steps {
                sh '''
                    docker run -d -p 8001:8000 --name test-app-${BUILD_NUMBER} simple-web-app:${BUILD_NUMBER}
                    sleep 5
                    docker exec test-app-${BUILD_NUMBER} curl -f http://localhost:8000/health || exit 1
                    docker stop test-app-${BUILD_NUMBER}
                    docker rm test-app-${BUILD_NUMBER}
                '''
            }
        }
    }
    
    post {
        success {
            echo '✅ Pipeline succeeded! Image ready for deployment.'
        }
        failure {
            echo '❌ Pipeline failed. Check logs above.'
        }
    }
}