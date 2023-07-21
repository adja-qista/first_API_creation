FROM python:3.9-slim-buster

# copy requirements, upgrade pip and install requirements.
COPY /requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Set work directory
WORKDIR /app
COPY . .
CMD uvicorn tuto:app --reload --host 0.0.0.0
EXPOSE 8000