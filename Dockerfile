FROM python:3.11-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

RUN useradd -m docker_user
USER docker_user

COPY app /app
COPY .env .env

EXPOSE 5000

ENV FLASK_ENV=production

CMD ["gunicorn", "app.run:app", "-b", "0.0.0.0:5000"]
