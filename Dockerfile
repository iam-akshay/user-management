FROM python:3.10.11-slim-bullseye as build-env

WORKDIR /app

COPY requirements.txt  /app/

RUN pip install -r requirements.txt

COPY .  /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]