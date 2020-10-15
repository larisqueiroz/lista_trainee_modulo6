FROM python:3.7-slim
#COPY . /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
WORKDIR /iris
COPY . .
