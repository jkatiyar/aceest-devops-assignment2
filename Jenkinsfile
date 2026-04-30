pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/jkatiyar/aceest-devops-assignment2.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t aceest-app .'
            }
        }

        stage('Push Docker Image') {
            steps {
                bat 'docker tag aceest-app jkatiyar007/aceest-app:latest'
                bat 'docker push jkatiyar007/aceest-app:latest'
            }
        }
    }
}