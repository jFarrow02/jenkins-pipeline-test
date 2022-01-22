@Library('jenkins-shared-library')

pipeline {

    agent any

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

        stage("deploy") {
            steps {
                script {
                    echo "deploying the application..."
                }
            }
        }
    }
}