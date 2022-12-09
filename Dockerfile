FROM python:3.8

WORKDIR /

COPY requirements.txt requirements.txt

#RUN apt-get update && \
#      apt-get -y install sudo \

#RUN sudo su
#RUN wget -q0 - https://dl.google.com/linux/linux_signing_key.pub | sudo gpg --dearmor -o /usr/share/keyrings/googlechrome-linux-keyring.gpg
#RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/googlechrome-linux-keyring.gpg] http://dl.google.com/linux/chrome/deb/stable main"
#RUN sudo tee /etc/apt/sources.list.d/google-chrome.list
#RUN sudo apt update
#RUN sudo apt install google-chrome-stable

RUN pip install -r requirements.txt

COPY ./src /src
COPY server.py server.py

CMD [ "python3", "server.py" ]