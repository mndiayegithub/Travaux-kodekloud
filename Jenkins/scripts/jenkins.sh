#!/bin/bash
#Installation link <https://pkg.jenkins.io/debian-stable/> / <https://www.jenkins.io/doc/book/installing/linux/#red-hat-centos>
#Install Java 11
sudo apt-get update -y
sudo add-apt-repository ppa:openjdk-r/ppa -y
sudo apt-get install fontconfig openjdk-11 -y

#Install jenkins
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee \
	/usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
    https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
    /etc/apt/sources.list.d/jenkins.list > /dev/null
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt install ca-certificates -y
sudo apt-get update -y
sudo apt-get install jenkins -y

#wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
#sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'