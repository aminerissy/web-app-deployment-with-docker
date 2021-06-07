FROM python:3.8-slim-buster
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip3 install -no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD [ "python3", "run.py" ]