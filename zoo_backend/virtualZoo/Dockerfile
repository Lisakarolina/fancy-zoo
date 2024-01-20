FROM python:3.8.3-slim

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /django_backend
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./virtualZoo/entrypoint.sh .
RUN sed -i 's/\r$//g' /django_backend/entrypoint.sh
RUN chmod +x /django_backend/entrypoint.sh
COPY . .

ENTRYPOINT ["/django_backend/entrypoint.sh"]