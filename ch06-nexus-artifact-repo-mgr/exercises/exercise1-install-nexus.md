## EXERCISE 1: Install Nexus on a server
If you already followed the demo in the Nexus module for installing Nexus, then you can use that one.

If not, you can watch the module demo video to install Nexus.
 ```
    history

    1  sudo apt update
    2  sudo apt install net-tools
    3  sudo apt install openjdk-8-jre-headless
    4  cd /opt
    5  sudo wget https://download.sonatype.com/nexus/3/latest-unix.tar.gz
    6  history
    7  ls -l
    8  sudo tar -zvxf latest-unix.tar.gz 
    9  ls -l
   10  sudo rm latest-unix.tar.gz 
   11  sudo adduser nexus
   12  ls -l
   13  sudo chown -R nexus:nexus nexus-3.37.3-02/
   14  sudo chown -R nexus:nexus sonatype-work/
   15  ls -l
   16  cd nexus-3.37.3-02/
   17  ls -l
   18  cd bin/
   19  ls -l
   20  nano nexus.rc
   21  ./nexus start
   22  cd ../../sonatype-work/
   23  ls -l
   24  cd nexus3/
   25  ls -l
   26  cat admin.password 
 ```
## EXERCISE 2: Create npm hosted repository
For a Node application you:

create a new npm hosted repository with a new blob store

## EXERCISE 3: Create user for team 1
You create Nexus user for the project 1 team to have access to this npm repository


## EXERCISE 4: Build and publish npm tar
You want to test that the project 1 user has correct access configured. So you:

build and publish a nodejs tar package to the npm repo

Hint:

```
# for publishing project tar file 
npm publish --registry={npm-repo-url-in-nexus} {package-name}
```

```
tar -cf <filename> <node-app-file/dir>

npm adduser --registry={npm-repo-url-in-nexus}
```

**In Nexus:**
Realms > add "npm Bearer Token Realm" to "Active" column

```
npm publish --registry={npm-repo-url-in-nexus} {tar-filename}

```

## EXERCISE 5: Create maven hosted repository
For a Java application you:

create a new maven hosted repository


## EXERCISE 6: Create user for team 2
You create a Nexus user for project 2 team to have access to this maven repository


## EXERCISE 7: Build and publish jar file
You want to test that the project 2 user has the correct access configured and also upload the first version. So:

build and publish the jar file to the new repository using the team 2 user.


Use: Java-Gradle application from Build Tools exercises



## EXERCISE 8: Download from Nexus and start application
Create new user for droplet server that has access to both repositories
On a digital ocean droplet, using Nexus Rest API, fetch the download URL info for the latest NodeJS app artifact
Execute a command to fetch the latest artifact itself with the download URL
Untar it and run on the server!
Hint:

```
# fetch download URL with curl
curl -u {user}:{password} -X GET 'http://{nexus-ip}:8081/service/rest/v1/components?repository={node-repo}&sort=version'
```




## EXERCISE 9: Automate
You decide to automate the fetching from Nexus and starting the application So you:

Write a script that fetches the latest version from npm repository. Untar it and run on the server!
Execute the script on the droplet
Hints:

```
# save the artifact details in a json file
curl -u {user}:{password} -X GET 'http://{nexus-ip}:8081/service/rest/v1/components?repository={node-repo}&sort=version' | jq "." > artifact.json

# grab the download url from the saved artifact details using 'jq' json processor tool
artifactDownloadUrl=$(jq '.items[].assets[].downloadUrl' artifact.json --raw-output)

# fetch the artifact with the extracted download url using 'wget' tool
wget --http-user={user} --http-password={password} $artifactDownloadUrl
```