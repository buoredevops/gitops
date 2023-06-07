FROM python:3.8-slim-buster
WORKDIR /demoapp
COPY  .  .
RUN apt-get -y install python3-pip \
   && pi3 install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]