FROM python:3.11.3-slim-buster
WORKDIR /demoapp
COPY  .  /demoapp
RUN  pip install --upgrade pip  \
     && pip3 install  Flask==2.3.1
RUN echo $PWD
RUN ls

EXPOSE 5000

ENV FLASK_APP=demoapp/app.py

CMD ["flask", "--app", "demoapp/app.py", "run", "--host=0.0.0.0"]