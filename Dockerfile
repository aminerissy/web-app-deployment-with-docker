FROM python:3.8-slim-buster
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8080
# ENTRYPOINT []
CMD [ "python3" ,"run.py" ]

# run docker in dev mode 
# docker run 
# -v /path/to/you/project:/path/folder/in/container 
# -p 8080:8080 <image-name>