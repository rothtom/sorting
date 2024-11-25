FROM python:3

RUN apt-get update -y && apt-get upgrade -y

COPY . /usr/sorting
WORKDIR /usr/sorting

RUN pip install --upgrade pip
RUN pip install -r requirements.txt