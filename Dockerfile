FROM python:3.10.10-slim-bullseye
COPY . .
RUN pip install -r requirements.txt
