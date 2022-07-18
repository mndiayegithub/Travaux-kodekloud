#!/bin/bash
sudo apt -yes update
sudo apt-get -yes install software-properties-common
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt-get -y install ansible