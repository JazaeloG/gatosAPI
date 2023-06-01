From python:3

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN mkdir /gatosapi

WORKDIR /gatosapi

COPY requirements.txt /gatosapi/

RUN pip install -r requirements.txt

COPY . /gatosapi/

CMD python manage.py runserver 0.0.0.0:8080
