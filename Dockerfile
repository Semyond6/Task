FROM python:3.10-slim

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# redis
ENV REDIS_OM_URL=redis://redis:6379/0

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .