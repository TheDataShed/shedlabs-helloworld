FROM python:2.7
ADD . /code 
WORKDIR /code
RUN pip install -r requirements.txt
RUN chmod +x ./run-django.sh
