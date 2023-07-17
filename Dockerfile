FROM python:3.9-slim-buster

# copy requirements, upgrade pip and install requirements.
COPY /requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Set work directory, copy source code to there
WORKDIR /app
COPY . .