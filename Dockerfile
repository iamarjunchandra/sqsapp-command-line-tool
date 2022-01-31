FROM python:3.8
COPY ./sqsapp ./sqsapp
RUN pip install boto3
RUN pip install typer
