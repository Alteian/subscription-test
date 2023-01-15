FROM python:3.11.1-buster

RUN mkdir /code

RUN pip install gunicorn

COPY requirements.txt ./

RUN python3 -m pip install -r requirements.txt

COPY ./ /code/

EXPOSE 8000
WORKDIR /code