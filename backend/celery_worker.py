from celery import Celery

celery = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)

# 🔥 IMPORTANT: tell Celery where tasks are
celery.autodiscover_tasks(["app.workers"])