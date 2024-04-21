FROM python:latest

WORKDIR /ciscapps/

ARG fullHostname
ARG hostname
ARG alphavantageKey
ARG serverPort

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD python3 api.py