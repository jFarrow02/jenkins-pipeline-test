# AWS and Jenkins - Deploy to EC2 Part II

Small applications with multiple containers would usually use `docker-compose`. How do we execute `docker-compose` on a remote server instance **from Jenkins**?

## Overview
1. Install `docker-compose` on EC2
2. Create `docker-compose.yml`
3. Adjust `Jenkinsfile` to execute `docker-compose` on EC2 instance

## Install docker-compose
1. SSH into EC2 instance and install `docker-compose` by downloading the binary:
    - `sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`

2. Apply executable permissions to the binary:
    - `sudo chmod +x /usr/local/bin/docker-compose`

3. Test the installation:
    - `docker-compose --version`

## Create docker-compose.yml in Source Code
On same level as `Jenkinsfile`:
1. `touch docker-compose.yaml`:

`docker-compose.yaml`:

```
version: '3.8'

services:
    java-maven-app:
        image: {image-name}:{tag-name}
        ports:
            - 8080:8080
        
    postgres:
        image: postgres:13
        ports:
            - 5432:5432
        environment:
            - POSTGRES_PASSWORD=my-pwd
```

## Adjust Jenkinsfile
In order to execute `docker-compose.yaml` on the EC2 instance, we need the file to exist **on the instance**.

1. Copy the `docker-compose.yaml` file **to EC2 from Jenkins**:

`Jenkinsfile`:

```
pipeline {
    // ...

    stage('deploy') {
        steps {
            script {
                def dockerComposeCmd = "docker-compose -f docker-compose.yaml up --detach"
                sshagent([ '{ssh-username-with-private-key-credential-name}']) {
                    sh "scp {docker-compose-file-location}.yaml {instance-username}@{instance-ip}:{instance-user-homedir}"
                    sh "ssh -o StrictHostKeyChecking=no {instance-username}@{instance-ip} ${dockerComposeCmd}" //Suppress popup

                }
            }
        }
    }
}

```

2. Commit and push Jenkinsfile and docker-compose.yaml changes and build Jenkins job.

## IMPROVEMENT: Extract to Shell Script
On same level as `Jenkinsfile`:

1. `touch server-commands.sh`:

```
#!/usr/bin/env bash

docker-compose -f docker-compose.yaml up --detach"
echo "success"
```

`Jenkinsfile`:

```
pipeline {
    // ...

    stage('deploy') {
        steps {
            script {
                echo 'deploying docker image to EC2...'
                def shellCmd = "bash ./server-cmds.sh"

                sshagent([ '{ssh-username-with-private-key-credential-name}']) {
                    sh "scp server-cmds.sh instance-username}@{instance-ip}:{instance-user-homedir}"
                    sh "scp {docker-compose-file-location}.yaml {instance-username}@{instance-ip}:{instance-user-homedir}"
                    sh "ssh -o StrictHostKeyChecking=no {instance-username}@{instance-ip} ${shellCmd}" //Suppress popup

                }
            }
        }
    }
}

```

2. Commit and push Jenkinsfile and `server-commands.sh` changes and build Jenkins job.

## IMPROVEMENT: Replace Docker image with newly-built version

`docker-compose.yaml`:

```
version: '3.8'

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

`server-cmds.sh`:

```
#!/usr/bin/env bash

export IMAGE=$1
docker-compose -f docker-compose.yaml up --detach"
echo "success"
```

`Jenkinsfile`:

```
pipeline {
    // ...

    stage('deploy') {
        steps {
            script {
                echo 'deploying docker image to EC2...'

                def shellCmd = "bash ./server-cmds.sh ${IMAGE_NAME}"

                sshagent([ '{ssh-username-with-private-key-credential-name}']) {
                    sh "scp server-cmds.sh instance-username}@{instance-ip}:{instance-user-homedir}"
                    sh "scp {docker-compose-file-location}.yaml {instance-username}@{instance-ip}:{instance-user-homedir}"
                    sh "ssh -o StrictHostKeyChecking=no {instance-username}@{instance-ip} ${shellCmd}" //Suppress popup

                }
            }
        }
    }
}

```

3. Commit and push Jenkinsfile and `server-commands.sh` changes and build Jenkins job.