FROM python:3.11-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /bot
COPY requirements.txt .
COPY . /bot
RUN pip  --no-cache -r /bot/requirements.txt && sudo apt-get redis-server \
    && sudo apt-get  redis-server && service sudo redis-server restart
CMD ["python", "-m", "bot"]

