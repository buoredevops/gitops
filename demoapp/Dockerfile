FROM python:3.11.3-slim-buster
WORKDIR /demoapp
COPY  .  .
RUN  pip install --upgrade pip  \
     && pip3 install  Flask==2.3.1

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]