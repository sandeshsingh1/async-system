from fastapi import APIRouter
from app.database import SessionLocal
from app.models import Document

router = APIRouter()

@router.get("/status/{doc_id}")
def get_status(doc_id: int):
    db = SessionLocal()

    doc = db.query(Document).filter(Document.id == doc_id).first()

    db.close()

    if not doc:
        return {"error": "Document not found"}

    return {
        "id": doc.id,
        "filename": doc.filename,
        "status": doc.status
    }