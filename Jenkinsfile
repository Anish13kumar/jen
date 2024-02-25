pipeline {
    agent any
    
    stages {
        stage('Remove Existing Container') {
            steps {
                script {
                    sh 'docker rm -f <container_name_or_id>'
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t <image_name>:<image_tag> .'
                }
            }
        }
        
        stage('Run New Container') {
            steps {
                script {
                    sh 'docker run -d -p 8000:8000 --name <container_name> <image_name>:<image_tag>'
                }
            }
        }
    }
}
