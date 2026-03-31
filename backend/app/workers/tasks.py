import time
import redis
from celery_worker import celery

from app.database import SessionLocal
from app.models import Document

r = redis.Redis(host="localhost", port=6379, db=0)


@celery.task
def process_document(doc_id):
    db = SessionLocal()

    def update_status(status):
        # Update DB
        doc = db.query(Document).filter(Document.id == doc_id).first()
        if doc:
            doc.status = status
            db.commit()

        # Publish event
        r.publish("progress", f"{doc_id}:{status}")

    try:
        update_status("processing")
        time.sleep(2)

        update_status("parsing")
        time.sleep(2)

        update_status("extracting")
        time.sleep(2)

        update_status("completed")

    except Exception:
        update_status("failed")

    finally:
        db.close()