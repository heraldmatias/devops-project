FROM python:3.9.10-slim-buster
WORKDIR /app
COPY . /app
#RUN apt-get install -y postgresql-devel
RUN pip install -r requirements.txt