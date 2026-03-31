from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Document
from ..workers.tasks import process_document

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload")
async def upload_file(file: UploadFile, db: Session = Depends(get_db)):
    doc = Document(filename=file.filename)
    db.add(doc)
    db.commit()
    db.refresh(doc)

    # Trigger background task
    process_document.delay(doc.id)

    return {"id": doc.id, "status": "queued"}