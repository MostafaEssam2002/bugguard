# BugGuard - Task Management API

## Overview

A RESTful API built with **FastAPI**, **SQLModel**, and **Pydantic**, providing task management features including CRUD operations, filtering, validation, and Docker support.

---

## Technologies Used

- FastAPI
- SQLModel (SQLAlchemy + Pydantic)
- Pydantic v2
- SQLite
- Docker
- Pytest

---

## Installation

```bash
git clone https://github.com/your-username/bugguard.git
cd bugguard
pip install -r requirements.txt
```

---

## Running the App Locally

```bash
python main.py
```

---

## Docker Usage

### Build the Docker Image

```bash
docker build -t bugguard-app .
```

### Run the Docker Container

```bash
docker run -d -p 8000:8000 bugguard-app
```

---

## Run Tests

```bash
python -m pytest
```

---

## API Endpoints

| Method | Endpoint                     | Description                        |
|--------|------------------------------|------------------------------------|
| GET    | `/`                          | Root API info                      |
| GET    | `/health`                    | Health check                       |
| POST   | `/tasks`                     | Create a new task                  |
| GET    | `/tasks`                     | List all tasks (with pagination)   |
| GET    | `/tasks/{task_id}`           | Retrieve task by ID                |
| PUT    | `/tasks/{task_id}`           | Update an existing task            |
| DELETE | `/tasks/{task_id}`           | Delete a task                      |
| GET    | `/tasks/status/{status}`     | Filter tasks by status             |
| GET    | `/tasks/priority/{priority}` | Filter tasks by priority           |

---

## Example cURL

```bash
curl -X POST "http://localhost:8000/tasks" \
-H "Content-Type: application/json" \
-d '{"title": "Fix login bug", "priority": "high", "status": "in_progress"}'
```

---

## Enum Values

### Task Status

- pending
- in_progress
- completed
- cancelled

### Task Priority

- low
- medium
- high
- urgent

---

## Pydantic Models

### TaskCreate

- `title`: str (required, max 200)
- `description`: str (optional, max 1000)
- `status`: enum (default: pending)
- `priority`: enum (default: medium)
- `due_date`: datetime (optional, must be in future)
- `assigned_to`: str (optional, max 100)

### TaskUpdate

All fields optional — same as `TaskCreate`.

### TaskResponse

Includes:
- `id`
- `created_at`
- `updated_at`

---

## 📁 Project Structure

```bash
bugguard/
├── main.py
├── models.py
├── schemas.py
├── database.py
├── test_main.py
├── requirements.txt
├── Dockerfile
├── .env
├── .dockerignore
└── README.md


## API Docs

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## Run in Production (Optional)

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## License

This project is part of the **FastAPI Intern Assessment**.

---

## Author

**The Mostafa Essam** 
