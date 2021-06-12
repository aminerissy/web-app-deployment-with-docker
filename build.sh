#!/bin/sh

python3 -m venv env
source ./env/bin/activate
# yum -y update
# yum -y install python3-pip
pip3 install -r requirements.txt