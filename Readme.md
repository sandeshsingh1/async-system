# 🚀 Async Document Processing System

## 📌 Overview

This is a full-stack asynchronous document processing system built using FastAPI, React, Celery, Redis, and PostgreSQL.

Users can upload documents, which are processed in the background. The system tracks job progress and allows retrying and exporting results.

---

## 🧠 Architecture

Frontend (React + TypeScript)
↓
FastAPI Backend (REST API)
↓
PostgreSQL (Database)
↓
Celery Workers (Async Processing)
↓
Redis (Broker + Pub/Sub)

---

## ⚙️ Tech Stack

### Backend

* FastAPI (Python)
* SQLAlchemy
* PostgreSQL
* Celery
* Redis

### Frontend

* React (TypeScript)
* Fetch API

---

## ✨ Features

* Upload documents
* Asynchronous background processing
* Job status tracking (Queued → Processing → Completed → Failed)
* Retry failed jobs
* Export processed data (JSON)
* Dashboard with auto-refresh

---

## 🔄 Workflow

1. User uploads a document
2. Backend stores metadata in PostgreSQL
3. Celery processes document asynchronously
4. Redis handles messaging
5. Status updates in database
6. Frontend displays progress

---

## 📡 API Endpoints

* POST `/upload` → Upload document
* GET `/documents` → List documents
* POST `/retry/{id}` → Retry job
* GET `/export/{id}` → Export JSON

---

## 🚀 Setup Instructions

### 1. Clone Repo

```bash
git clone https://github.com/<your-username>/async-system.git
cd async-system
```

---

### 2. Backend Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate

pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic celery redis python-multipart
```

---

### 3. Start PostgreSQL

```bash
sudo service postgresql start
```

Create DB:

```bash
sudo -u postgres psql
```

```sql
CREATE DATABASE docdb;
ALTER USER postgres PASSWORD 'password';
\q
```

---

### 4. Start Redis

```bash
redis-server
```

---

### 5. Start Celery

```bash
python -m celery -A celery_worker.celery worker --loglevel=info
```

---

### 6. Start Backend

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

---

### 7. Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 🌐 Access

Backend Docs:
http://<your-ip>:8000/docs

Frontend:
http://localhost:5173

---

## 📌 Assumptions

* Processing logic is simulated
* Single worker
* Polling used instead of WebSockets

---

## ⚠️ Limitations

* No authentication
* Files not stored permanently
* Basic UI

---

## 💡 Future Improvements

* WebSockets for real-time updates
* File storage (S3/local)
* Authentication system
* Docker setup

---

## 🎥 Demo

(Add your demo video link here)

---

## 🏁 Conclusion

This project demonstrates asynchronous processing, backend architecture design, and integration of API, database, and background workers.
