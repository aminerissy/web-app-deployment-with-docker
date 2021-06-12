FROM python:3.8-slim-buster
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apt -y update
RUN apt -y install python3-pip
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8080
CMD [ "python3", "run.py" ]
