FROM python:3.8-slim-buster
COPY requirements.txt /app
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8080
ENTRYPOINT ["python3"]
CMD [ "run.py" ]
