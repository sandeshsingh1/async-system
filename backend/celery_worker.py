from celery import Celery

celery = Celery(
    "worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)

# 🔥 IMPORTANT: tell Celery where tasks are
celery.autodiscover_tasks(["app.workers"])