from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import upload, jobs, status, export
from app.database import Base, engine

# ✅ Create app ONCE
app = FastAPI()

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Create tables
Base.metadata.create_all(bind=engine)

# ✅ Routes
app.include_router(upload.router)
app.include_router(jobs.router)
app.include_router(status.router)
app.include_router(export.router)


@app.get("/")
def root():
    return {"message": "Backend running"}