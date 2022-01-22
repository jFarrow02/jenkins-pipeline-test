pipeline {

    agent any

    tools {
        maven "maven-latest"
    }

    stages {
        stage("test") {
            script {
                echo "testing the application..."
            }
        }

        stage("build") {
            script {
                echo "building the application..."
            }
        }

        stage("deploy") {
            script {
                echo "deploying the application..."
            }
        }
    }
}