FROM python:3.11-bullseye

RUN pip install Flask==2.2.3 Flask-SQLAlchemy Flask-Migrate flask-login mysqlclient


WORKDIR /app
COPY app.py app.py
COPY templates templates

EXPOSE 8080

CMD ["python", "app.py"]