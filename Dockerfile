FROM python:3.8

WORKDIR /

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./src /src
COPY server.py server.py

CMD [ "python3", "server.py" ]