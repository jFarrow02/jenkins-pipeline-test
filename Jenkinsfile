pipeline {

    agent any

    tools {
        maven "maven-latest"
    }

    stages {
        stage("test") {
            steps {
                script {
                    echo "testing the application..."
                    sh 'mvn test'
                }
            }
        }

        stage("build") {
            steps {
                script {
                    echo "building the application..."
                    'mvn package'
                }
            }
        }

        stage("deploy") {
            steps {
                script {
                    echo "deploying the application..."
                }
            }
        }
    }
}