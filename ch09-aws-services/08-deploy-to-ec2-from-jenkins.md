# AWS and Jenkins - Deploy to EC2

## Steps
1. Connect to EC2 instance from Jenkins server via ssh
2. Execute `docker run` on EC2 instance

### Install SSH Agent Plugin

In Jenkins:
- Dashboard > Plugin Manager > search for SSH Agent > Install w/o restart
- Create credentials (.pem file) for EC2:
    - {multibranch-pipeline-name} > Credentials > Folder > Global credentials
    - select "SSH username with private key"
    - "Username": same as ssh user you use to connect to EC2 instance from terminal
    - "Private key" > "enter directly"
    - Copy content of your .pem file and paste > OK
- Use credential in Jenkinsfile and write command to ssh:
    - {multibranch-pipeline-name} > Pipeline Syntax > Sample Step > sshAgent
    - Select your ssh credential > Generate Pipeline Script

### Prepare Jenkinsfile and EC2 Instance

- `docker login` on EC2 instance
- Configure security rule to allow SSH access to EC2 from Jenkins server's IP address


`Jenkinsfile`:

```
pipeline {
    // ...

    stage('deploy') {
        steps {
            script {
                def dockerCmd = 'docker run -d -p {port}:{port} {image-name}:{tag-name}'
                sshagent([ '{ssh-username-with-private-key-credential-name}']) {
                    sh "ssh -o StrictHostKeyChecking=no {instance-username}@{instance-ip} ${dockerCmd}" //Suppress popup

                }
            }
        }
    }
}

```
- Run Jenkins build

## Some Notes:

1. Deploying app using SSH is applicable for **all servers or cloud providers**
2. Simple use case:
    - connect to server and start 1 Docker container
    - good for smaller projects
    - Deployment looks different for tens or 100s of containers
    - Container orchestration tool like K8s is needed
3. Using docker compose for deployment:
    - from Git repo, copy docker-compose to EC2 after ssh-ing into it, and execute docker-compose command on EC2 from sshagent block