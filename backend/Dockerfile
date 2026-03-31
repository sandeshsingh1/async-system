FROM python:3.11-slim

WORKDIR /app

COPY . /app

ENV PYTHONPATH=/app

RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy psycopg2-binary pydantic celery redis python-multipart

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]