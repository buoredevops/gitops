FROM python:3.11.3-slim-buster
WORKDIR /app
COPY  .  /app
RUN  pip install --upgrade pip  \
     && pip3 install  Flask==2.3.1

CMD ["flask", "--app", "app.py", "run", "--host=0.0.0.0"]