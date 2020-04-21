FROM python:3-alpine

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD . /app/
CMD python /app/manage.py runserver 0.0.0.0:8000