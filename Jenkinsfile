pipeline {
    agent any
    
    stages {
        stage('Remove Existing Container') {
            steps {
                script {
                    sh 'docker rm -f jenk'
                    echo 'removed existing'
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t jen .'
                    echo 'build success'

                }
            }
        }
        
        stage('Run New Container') {
            steps {
                script {
                    sh 'docker run -d --name jen jenk'
                    echo 'container running'
                }
            }
        }
    }
}
