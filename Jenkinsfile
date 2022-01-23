@Library('jenkins-shared-library')_

pipeline {

    agent any

    environment {
        NEXUS_REPO = "35.153.127.31:8083"
        TAG = "1.0"
        IMAGE = "${NEXUS_REPO}/java-maven-app:${TAG}"
    }
    tools {
        maven "maven-latest"
    }

    stages {

        stage("build") {
            steps {
                script {
                    echo "testing and packaging the application..."
                    testAndPackage()
                }
            }
        }

        stage("buildImage") {
            steps {
                script {
                    echo "building image $IMAGE..."
                    buildImage(IMAGE, NEXUS_REPO)
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