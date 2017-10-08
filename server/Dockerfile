FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends python-pip python-setuptools

RUN pip install --upgrade pip
RUN mkdir /code
ADD reqs.txt /tmp/
RUN pip install -r /tmp/reqs.txt
ADD . /code
WORKDIR /code
ENV FLASK_APP /code/src/app.py
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
