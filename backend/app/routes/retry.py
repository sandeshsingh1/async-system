from fastapi import APIRouter
from app.database import SessionLocal
from app.models import Document
from app.workers.tasks import process_document

router = APIRouter()

@router.post("/retry/{doc_id}")
def retry(doc_id: int):
    db = SessionLocal()

    doc = db.query(Document).filter(Document.id == doc_id).first()

    if not doc:
        return {"error": "Not found"}

    doc.status = "pending"
    db.commit()

    process_document.delay(doc_id)

    db.close()

    return {"message": "Retry started"}