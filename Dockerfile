FROM python:3.7.13-slim as production

ENV PYTHONBUFFERED=1

RUN apt-get update && \
    apt-get install -y \
    bash \
    build-essential \
    gcc \
    libffi-dev \
    musl-dev \
    openssl \
    postgresql \
    libpq-dev

WORKDIR /app/
COPY requirements/prod.txt ./prod.txt
RUN pip install -r prod.txt

COPY manage.py ./manage.py
COPY alan_website ./alan_website

EXPOSE 8000

FROM production as development

COPY requirements/dev.txt ./dev.txt
RUN pip install -r ./dev.txt

COPY . .


