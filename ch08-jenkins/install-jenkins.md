# Installing Jenkins

2 ways to install Jenkins:
1. Install Jenkins directly on OS
2. Run Jenkins as Docker containers

## Create a Jenkins Server in the Cloud

1. At least 2GB RAM
2. Firewall rules:
    - SSH on port 22
    - Custom TCP: port 8080 for incoming requests

3. Install Docker
    - `sudo apt install docker.io`

4. Create new Jenkins user and add to docker group:
    - `sudo adduser jenkins`
    - `sudo usermod -aG docker jenkins`
    - Log out and restart server.

    - `su jenkins`
    - `docker run -p 8080:8080 -p 50000:50000 -d -v jenkins_home:/var/jenkins_home jenkins/jenkins`

5. Visit Jenkins server IP on port 8080 in browser. Enter admin password from location indicated or `docker logs {container_name}`

6. Install suggested plugins.