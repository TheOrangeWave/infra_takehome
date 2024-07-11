# syntax=docker/dockerfile:1

FROM python:3.9


WORKDIR /birdyapp/


COPY ./requirements.txt /birdyapp/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /birdyapp/requirements.txt

 
COPY . /birdyapp/app

# USER root

# RUN pip3 install Flask

WORKDIR app

CMD ["python3", "/usr/local/bin/flask", "run", "--host", "0.0.0.0", "--port", "3000"]
