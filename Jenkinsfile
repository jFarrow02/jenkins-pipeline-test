pipeline {

    agent any

    tools {
        maven "maven-latest"
    }

    stages {
        stage("test") {
            stages {
                script {
                    echo "testing the application..."
                }
            }
        }

        stage("build") {
            script {
                stages {
                    echo "building the application..."
                }
            }
        }

        stage("deploy") {
            script {
                stages {
                    echo "deploying the application..."
                }
            }
        }
    }
}