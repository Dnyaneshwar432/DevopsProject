pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build JAR') {
            steps {
                echo 'Building JAR using Maven...'
                sh 'mvn clean install'
            }
        }

        stage('Create JAR file') {
            steps {
                sh 'ls -l target/*.jar'
            }
        }
    }

    post {
        success {
            echo ' JAR Build successful!'
        }
        failure {
            echo ' Build failed!'
        }
    }
}
