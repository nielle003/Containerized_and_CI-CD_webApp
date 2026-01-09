pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    
    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    pip install --no-cache-dir -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh '''
                    apt-get update && apt-get install -y docker.io
                    docker build -t simple-web-app:${BUILD_NUMBER} .
                '''
            }
        }
        
        stage('Test Docker Container') {
            steps {
                sh '''
                    apt-get install -y curl
                    docker run -d -p 8001:8000 --name test-app-${BUILD_NUMBER} simple-web-app:${BUILD_NUMBER}
                    sleep 5
                    curl http://localhost:8001/health
                    docker stop test-app-${BUILD_NUMBER}
                    docker rm test-app-${BUILD_NUMBER}
                '''
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        success {
            echo 'Pipeline succeeded! Image ready for deployment.'
        }
        failure {
            echo 'Pipeline failed. Check logs above.'
        }
    }
}