FROM python:3.11-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /bot
COPY requirements.txt .
COPY . /bot
RUN pip  --no-cache -r /bot/requirements.txt &&  apt-get  redis-server \
    && apt-get  redis-server && service redis-server restart
CMD ["python", "-m", "bot"]

