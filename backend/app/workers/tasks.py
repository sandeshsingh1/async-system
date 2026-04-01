import time
import os
import redis

from celery_worker import celery
from app.database import SessionLocal
from app.models import Document

# ✅ Redis connection (Docker-safe)
r = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379,
    db=0,
    decode_responses=True  # 🔥 important (strings instead of bytes)
)


@celery.task
def process_document(doc_id: int):
    db = SessionLocal()

    def update_status(status: str):
        # 🔹 Update DB
        doc = db.query(Document).filter(Document.id == doc_id).first()
        if doc:
            doc.status = status
            db.commit()

        # 🔹 Publish event (for realtime UI later)
        r.publish("progress", f"{doc_id}:{status}")

        print(f"[TASK] Doc {doc_id} → {status}")  # 🔥 debug log

    try:
        update_status("processing")
        time.sleep(2)

        update_status("parsing")
        time.sleep(2)

        update_status("extracting")
        time.sleep(2)

        update_status("completed")

    except Exception as e:
        print(f"[ERROR] {e}")
        update_status("failed")

    finally:
        db.close()