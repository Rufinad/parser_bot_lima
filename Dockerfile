FROM python:3.11-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /bot
COPY requirements.txt .
COPY . /bot
RUN pip install --no-cache -r /bot/requirements.txt
CMD ["python", "-m", "bot"]

