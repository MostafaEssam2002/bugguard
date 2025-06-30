import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel
from datetime import datetime, timedelta, timezone
from main import app
from database import engine

client = TestClient(app)

@pytest.fixture(autouse=True)
def fresh_db():
    SQLModel.metadata.drop_all(bind=engine)
    SQLModel.metadata.create_all(bind=engine)
    yield
    SQLModel.metadata.drop_all(bind=engine)

def create_task(title: str = "T", priority="medium", status="pending", **extra):
    payload = {
        "title": title,
        "priority": priority,
        "status": status,
        **extra,
    }
    return client.post("/tasks", json=payload)

def test_root_and_health():
    assert client.get("/").status_code == 200
    assert client.get("/health").json() == {"status": "OK"}

@pytest.mark.parametrize(
    "payload",
    [
        {"title": ""},                         
        {"title": "  "},                      
        {
            "title": "Past due",
            "due_date": (datetime.now(timezone.utc) - timedelta(days=1)).isoformat(),
        },                                    
        {"title": "Bad status", "status": "x"},  
    ],
)
def test_create_task_validation_errors(payload):
    response = client.post("/tasks", json=payload)
    assert response.status_code == 422

# ---------- CRUD (404) ---------- #
def test_get_update_delete_nonexistent():
    assert client.get("/tasks/999").status_code == 404
    assert client.put("/tasks/999", json={"title": "X"}).status_code == 404
    assert client.delete("/tasks/999").status_code == 404

# Pagination 
def test_pagination_skip_limit():
    # create 15 task 
    for i in range(15):
        create_task(title=f"T{i}")
    resp = client.get("/tasks", params={"skip": 5, "limit": 5})
    data = resp.json()
    assert resp.status_code == 200
    assert len(data) == 5
    assert data[0]["title"] == "T5"

# ---------- Sorting ---------- #
def test_sort_by_due_date():
    now = datetime.now(timezone.utc)
    create_task(title="early", due_date=(now + timedelta(days=1)).isoformat())
    create_task(title="late", due_date=(now + timedelta(days=5)).isoformat())
    resp = client.get("/tasks", params={"sort_by": "due_date"})
    titles = [t["title"] for t in resp.json()]
    assert titles == ["early", "late"]

# ---------- Search ---------- #
def test_search_term():
    create_task(title="Fix login bug")
    create_task(title="Write docs")
    resp = client.get("/tasks", params={"search": "login"})
    data = resp.json()
    assert len(data) == 1
    assert data[0]["title"] == "Fix login bug"


def test_filter_status_and_priority_combined():
    create_task(title="A", status="in_progress", priority="high")
    create_task(title="B", status="pending", priority="high")
    create_task(title="C", status="in_progress", priority="low")
    resp = client.get(
        "/tasks",
        params={"status": "in_progress", "priority": "high"},
    )
    titles = [t["title"] for t in resp.json()]
    assert titles == ["A"]