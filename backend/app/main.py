from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import upload, jobs
from .database import Base, engine

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Enable CORS (frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router)
app.include_router(jobs.router)

@app.get("/")
def root():
    return {"message": "Backend running"}