FROM python:3.11.1-buster

RUN mkdir /code

RUN pip install gunicorn

COPY requirements.txt ./
# COPY requirements.txt requirements.txt
# Use copy instead of add
RUN python3 -m pip install -r requirements.txt

# COPY . .
COPY ./ /code/

WORKDIR /code