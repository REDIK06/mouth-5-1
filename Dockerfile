FROM python:3.9

ENV PYTHONWRITEBYTECODE 1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r /app/requirements.txt

COPY . .