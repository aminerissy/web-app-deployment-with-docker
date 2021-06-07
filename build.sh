#!/bin/sh

python3 -m venv env
source ./env/bin/activate
apt update
apt -y install python3-pip
pip3 install -r requirements.txt