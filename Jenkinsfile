pipeline {
    agent any

    environment {
        IMAGE_NAME = 'journalapp'
        CONTAINER_NAME = 'journalapp-container'
        DOCKERHUB_USER = 'dnyaneshwar432'  
    }

    stages {

        stage('Build JAR') {
            steps {
                echo '🔨 Building Spring Boot app...'
                sh 'mvn clean install'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Remove Old Container') {
            steps {
                echo '🧹 Cleaning up old container (if any)...'
                sh """
                    docker rm -f ${CONTAINER_NAME} || true
                """
            }
        }

        stage('Run Docker Container') {
            steps {
                echo '🚀 Running Docker container...'
                sh """
                    docker run -d --name ${CONTAINER_NAME} ${IMAGE_NAME}
                """
            }
        }

        // Optional stage to push image to DockerHub (needs credentials)
        stage('Push to DockerHub') {
            when {
                expression { return env.DOCKERHUB_USER != 'dnyaneshwar432' }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    echo '📤 Pushing image to DockerHub...'
                    sh """
                        docker login -u $DOCKER_USER -p $DOCKER_PASS
                        docker tag ${IMAGE_NAME}:latest $DOCKER_USER/${IMAGE_NAME}
                        docker push $DOCKER_USER/${IMAGE_NAME}
                    """
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline complete! App is built, containerized, and running!'
        }
        failure {
            echo '❌ Something went wrong in the pipeline.'
        }
    }
}
