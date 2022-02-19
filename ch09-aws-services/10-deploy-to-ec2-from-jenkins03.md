# AWS and Jenkins - Deploy to EC2 Part III

`Jenkinsfile`:
```groovy

#!/usr/bin/env groovy

library identifier: 'jenkins-shared-library@master', retriever: modernSCM(
    [
        $class: 'GitSCMSource',
        remote: 'https://gitlab.com/nanuchi/jenkins-shared-library.git',
        credentialsId: 'gitlab-credentials'
    ]
)

pipeline {
    agent any
    tools: {
        maven 'Maven'
    }

    stages {
        stage("increment version") {
            steps {
                script {
                    echo "incrementing app version..."
                     sh 'mvn build-helper:parse-versionversions:set \
                     -DnewVersion=\\\${parsedVersionmajorVersion}.\\\${parsedVersionminorVersion}.\\\${parsedVersionnextIncrementalVersion} \
                     versions:commit'
                     
                     // Read the version number from pom.xml
                     def matcher = readFile('pom.xml') =~'<version>(.+)</version>'
                     // Returns an array of matched tags andchildren tags inside
                     def version = matcher[0][1] // 0.0.0
                     env.IMAGE_NAME = "$version-$BUILD_NUMBER" / 0.0.0-{jenkins-build-number}
                }
            }
        }

        stage('build app') {
            steps {
                script {
                    echo 'buidling application jar...'
                    buildJar()
                }
            }
        }

        stage('build image') {
            steps {
                script {
                    echo 'building docker image...'
                    buildImage(env.IMAGE_NAME)
                    dockerLogin()
                    dockerPush(env.IMAGE_NAME)
                }
            }
        }

        stage('deploy') {
            steps {
                script {
                    echo 'deploying docker image to EC2...'

                    def shellCmd = "bash ./server-cmds.sh ${IMAGE_NAME}"
                    def ec2Instance = "ec2-user@{INSTANCE_IP}"

                    sshagent(['ec2-server-key']) {
                        sh "scp server-cmds.sh ${ec2Instance}:/home/ec2-user"
                        sh "scp docker-compose.yaml ${ec2Instance}:/home/ec2-user"
                        sh "ssh -o StrictHostKeyChecking=no ${ec2Instance} ${shellCmd}"
                    }
                }
            }
        }

        stage('commit version update') {
                steps {
                    script {
                        withCredentials([ credentialsId: '{git-credentials-id}', usernameVariable: 'USER', passwordVariable: 'PWD']) {

                            // Set global git config, OR ssh into jenkins server and set
                            sh 'git config --global user.email "jenkins@example.com"'
                            sh 'git config --global user.name "jenkins"'


                            // commit changes from Jenkinsfile
                            sh "git remote set-url origin https://$USER:$PWD@{git-repo-url}" // set repo url for current context and pass credentials for auth
                            sh 'git add .'
                            sh "git commit -m"ci: version bump"
                            sh "git push origin HEAD:${BRANCH_NAME}" // Use "BRANCH_NAME" Jenkins env var
                        }
                    }
                }
            }

    }
}
```

`server-cmds.sh`
```sh
#!/usr/bin/env bash

export IMAGE=$1
docker-compose -f docker-compose.yaml up --detach
echo "success"
```

`docker-compose.yaml`:
```yaml
version '3.8'
services:
    java-maven-app:
        image: ${IMAGE}
        ports:
            - 8080:8080
    postgres:
        image: postgres:13
        ports:
            - 5432:5432
        environment:
            - POSTGRES_PASSWORD=my-pwd
```

