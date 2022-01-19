# Making Docker Available in Jenkins

In most scenarios, you will want to build Docker images of your applications in Jenkins (to push to artifact repos). To do so, Docker commands must be available in Jenkins.

The most common way to do this is to **mount a Docker volume from your server instance to the Jenkins container running on it.**

- Must **stop** the currently-running Jenkins container (if applicable), **mount** the new volume **and** the current volume (with the saved data/configuration for Jenkins), and start a new container.