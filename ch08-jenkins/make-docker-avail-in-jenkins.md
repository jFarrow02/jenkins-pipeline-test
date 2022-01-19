# Making Docker Available in Jenkins

In most scenarios, you will want to build Docker images of your applications in Jenkins (to push to artifact repos). To do so, Docker commands must be available in Jenkins.

The most common way to do this is to **mount a Docker volume from your server instance to the Jenkins container running on it.**

- Must **stop** the currently-running Jenkins container (if applicable), **mount** the new volume **and** the current volume (with the saved data/configuration for Jenkins) from server host, and start a new container.

## Stopping Container and Attaching New Volume

1. `docker ps` (Get running container ID)
2. `docker stop {container_id}`
3. `docker run -p 8080:8080 -p 50000:50000 -d -v jenkins_home:var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock -v $(which docker):/usr/bin/docker jenkins/jenkins`
    - /var/run/docker.sock: Docker volume
    - $(which docker): Docker runtime binary