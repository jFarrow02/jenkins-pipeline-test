#!/bin/bash

# update apt
sudo apt update -y

# install nettools
sudo apt install -y net-tools

# install Java 8 (required version for Nexus)
sudo apt install -y openjdk-8-jre-headless

java_version=$(java -version)

echo "Java version installed: $(java -version)"

# Create new user
NEW_USER=nexususer

# add new user and create home directory (-m flag)
sudo useradd $NEW_USER -m
# sudo echo $NEW_USER:duracell99 | chpasswd

# download Nexus and install as new user
cd /opt/
echo "Downloading nexus tar file..."
sudo wget -x https://download.sonatype.com/nexus/3/latest-unix.tar.gz


#untar
if [ -f download.sonatype.com/nexus/3/latest-unix.tar.gz ]
then
        echo  "Untarring file..."
        sudo tar -zvxf download.sonatype.com/nexus/3/latest-unix.tar.gz
        echo "Removing tar file..."
        sudo rm download.sonatype.com/nexus/3/latest-unix.tar.gz
fi


# change permissions for nexus and soanatype-work dirs
nexusdir=nexus-3.37.3-02
sonatypedir=sonatype-work

#echo "Changing owner to nexususer..."
#sudo chown -R nexususer:nexususer $nexusdir
#sudo chown -R nexususer:nexususer $sonatypedir

# switch to nexususer
su $NEW_USER
cat "run_as_user=\"$NEW_USER\"" > $nexusdir/bin/nexus.rc

# start nexus service
echo "Starting nexus service..."
/opt/nexus-3.37.3-02/nexus start

ps aux | grep nexus

netstat -lnpt
