from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Document
from app.workers.tasks import process_document
from fastapi.responses import JSONResponse


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/documents")
def get_docs(db: Session = Depends(get_db)):
    return db.query(Document).all()

@router.post("/retry/{doc_id}")
def retry_job(doc_id: int):
    process_document.delay(doc_id)
    return {"message": "Retry started"}
@router.get("/export/{doc_id}")
def export_doc(doc_id: int, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == doc_id).first()
    return JSONResponse(content={
        "id": doc.id,
        "filename": doc.filename,
        "status": doc.status
    })