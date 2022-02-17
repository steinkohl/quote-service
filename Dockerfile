# syntax=docker/dockerfile:1

FROM python:3.9

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 50051

CMD [ "python3", "quote_server.py"]