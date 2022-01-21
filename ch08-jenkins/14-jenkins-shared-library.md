# Jenkins Shared Library

A way to:
- Avoid repeating the same pipeline building logic across multiple similar projects

## What is Jenkins Shared Library?
- an extension to the pipeline
- has its own repository
- written in Groovy
- write all shared logic in shared library and reference it in each project's Jenkinsfile

## Steps to Using Jenkins Shared Library

1. Create the Shared Library (SL)
2. Make SL available in Jenkins
3. Use the SL in Jenkinsfile

## Create Shared Library
1. Create repo
2. Write Groovy Code
3. Make SL available (globally or for project)
4. Use SL in Jenkinsfile

### 1. Create repo
- Create Git repo in SCM for your shared library and push the below project.

### 2. Write Groovy Code
- Create new Groovy project (IntelliJ, etc.)
- Project structure:
```
|-src   // helper logic, utilities etc
    |-com
        |-example
            |-ClassName.groovy  // Groovy class with extracted logic
|-vars // functions we call from Jenkinsfile
    |-function1.groovy  // each function/execution step is its own Groovy file
    |-function2.groovy
    |-function3.groovy
|-resources // External libs and non-Groovy files (SQL scripts, shell scripts, JSON files etc.)

```

`/vars/buildJar.groovy`:

```
#!/usr/bin/env groovy

def call() {
    echo "building the JAR file for the application..."
    sh "mvn package"
}
```

`/vars/buildImage.groovy`:

```
#!/usr/bin/env groovy

def call() {
    echo "building the docker image..."
    withCredentials([usernamePassword(credentialsId: 'docker-hub-repo', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
        sh 'docker build -t nanajanashia/demo-app:jma-2.0 .'
        sh "echo $PASS | docker login -u $USER --password-stdin"
        sh 'docker push nanajanashia/demo-app:jma-2.0'
    }
}
```

### Make Shared Library Globally Available for use in Jenkinsfile
E.g. for company-wide shared libraries:

1. Manage Jenkins > Configure System > Global Pipeline Libraries
    - Default Version: A default version of the library to load if a script does not select another. Might be a branch name, tag, commit hash, etc., according to the SCM. **Recommended:** use a **fixed version** to avoid potential breaking changes when updates made to library

### 3. Use Shared Library in Jenkinsfile

`Jenkinsfile`:

```
@Library("jenkins-shared-library") // If pipeline is direct next step, annotation must end with "_"
def gv

pipeline {

    agent any

    environment {
        NEXUS = "18.221.41.70:8083"
        IMAGE = "$NEXUS/java-maven-app:latest"
    }

    tools {
        maven "maven-3.8.4(default)"
    }
    stages {

        stage("init") {
            steps {
                script {
                    gv = load "script.groovy"
                }
            } 
        }

        stage("build jar") {
            steps {
                script {
                    echo "executing pipeline for branch $BRANCH_NAME"
                    buildJar()
                }
            }
        }

        stage("build image") {
            steps {
                script {
                    buildAndPushImage(IMAGE, NEXUS)
                }
            }
        }

        stage("deploy") {
            steps {
                script {
                    gv.deployApp()
                }
            }
        }
    }
}

```

#### Recommended: Extract logic to Groovy Classes
You can use Groovy classes to group shared logic to avoid duplication where needed.

`src/com/example/Docker.groovy`:

```
#!/usr/bin/env groovy
package com.example

class Docker implements Serializable { // supports saving state if pipeline is paused and resumed

    def script // Makes env vars, commands, etc. from pipeline syntax available in class

    Docker(script) {
        this.script = script
    }

    def buildDockerImage(String imageName, String repoLocation) {
        script.echo "building the docker image..."
        script.withCredentials([script.usernamePassword(credentialsId:    'nexus-my-docker-hostedrepo', passwordVariable: 'PWD',     usernameVariable: 'USER')]) {
            script.sh "docker build -t $imageName ."
            script.sh "echo $script.PWD | docker login -u $script.USER --password-stdin  $repoLocation"
            script.sh 'docker push $imageName'
        }
    }
}

```

`/vars/buildImage.groovy`:

```
#!/usr/bin/env groovy

import com.example.Docker

def call(String imageName, String repoLocation) {
    return new Docker(this).buildDockerImage(imageName, repoLocation)
}
```

#### Optional: Project-scoped Shared Library
In the case that the shared library will not be used by other teams or by many other projects, this is an alternative to defining a global shared library.

1. Delete Global library from Configure System:
    - Dashbord > Manage Jenkins > Configure System > Delete library

2. Reference library directly in Jenkinsfile:

`Jenkinsfile`:

```
library identifier: 'jenkins-shared-library@{version}', retriever: modernSCM(
    [ 
        $class: 'GitSCMSource',
        remote: '{shared-lib-repo-url}'
        credentialsId: '{jenkins-git-credentials-id}'
    ]
)
// version: can be a branch, tag, or commit hash

def gv

pipeline { // ... }

}
```