# 🚀 Async Document Processing System

A production-style asynchronous backend system built using **FastAPI, Celery, Redis, PostgreSQL, and Docker**.
This system allows users to upload documents, process them asynchronously, and retrieve results without blocking the API.

---

## 🧠 Overview

This project demonstrates how to build a **scalable async system** where:

* Users upload documents via API
* Backend stores metadata in PostgreSQL
* Heavy processing runs in background using Celery
* Redis acts as a message broker
* System is fully containerized using Docker

---

## ⚙️ Tech Stack

* **Backend:** FastAPI
* **Async Processing:** Celery
* **Message Broker:** Redis
* **Database:** PostgreSQL
* **Containerization:** Docker + Docker Compose
* **Frontend (optional):** React (Vite)

---

## 📁 Project Structure

```
async-system/
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── workers/
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── main.py
│   │
│   ├── celery_worker.py
│   ├── Dockerfile
│   ├── requirements.txt
│
├── frontend/
│
├── docker-compose.yml
└── README.md
```

---

## 🚀 Features

* 📄 Upload documents via API
* ⚡ Asynchronous background processing
* 🔄 Task queue using Celery + Redis
* 🗄️ Persistent storage with PostgreSQL
* 🐳 Fully Dockerized microservices
* 📊 Scalable architecture

---

## 🧪 API Endpoints

### 🔹 Upload File

```
POST /upload
```

### 🔹 Get Documents

```
GET /documents
```

### 🔹 Health Check

```
GET /
```

---

## 🐳 Running with Docker

### Step 1: Start services

```
docker-compose up --build
```

### Step 2: Open API docs

```
http://localhost:8000/docs
```

---

## ⚠️ Important Configuration

### Database (Docker)

```
postgresql://postgres:password@db:5432/docdb
```

### Redis (Docker)

```
redis://redis:6379/0
```

---

## 🔄 How It Works

1. User uploads a file via `/upload`
2. File metadata is stored in PostgreSQL
3. A Celery task is triggered
4. Task is sent to Redis queue
5. Worker picks the task
6. Background processing happens
7. Result is stored/updated

---

## 🧠 Architecture

```
Client → FastAPI → Redis Queue → Celery Worker → PostgreSQL
```

---

## 📦 Worker Logs Example

```
Task received
Processing document...
Task succeeded
```

---

## 🎯 Key Learning Outcomes

* Asynchronous task processing
* Microservices communication
* Docker-based deployment
* Queue-based architecture
* Backend scalability patterns

---

## 💡 Future Improvements

* Add task status tracking API
* Add frontend UI for uploads
* Add authentication
* Add file storage (S3/local)
* Add retry & failure handling

---

## 👨‍💻 Author

**Sandesh Singh**

---

## ⭐ Conclusion

This project demonstrates a real-world backend system design using asynchronous processing and distributed services. It highlights scalability, performance optimization, and clean architecture practices used in modern backend systems.
