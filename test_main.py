from fastapi.testclient import TestClient
from main import app
client = TestClient(app)
# test data
task_data = {
    "title": "Test Task",
    "description": "This is a test task",
    "priority": "high",
    "status": "in_progress"
}
def test_create_task():
    response = client.post("/tasks", json=task_data)
    assert response.status_code == 201
    assert response.json()["title"] == task_data["title"]

def test_get_all_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_task_by_id():
    response = client.post("/tasks", json=task_data)
    task_id = response.json()["id"]
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 200
    assert get_response.json()["id"] == task_id

def test_update_task():
    response = client.post("/tasks", json=task_data)
    task_id = response.json()["id"]
    updated_data = {"title": "Updated Task", "priority": "urgent"}
    update_response = client.put(f"/tasks/{task_id}", json=updated_data)
    assert update_response.status_code == 200
    assert update_response.json()["title"] == "Updated Task"
    assert update_response.json()["priority"] == "urgent"
def test_delete_task():
    response = client.post("/tasks", json=task_data)
    task_id = response.json()["id"]
    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == f"Task {task_id} deleted"
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404

def test_filter_by_status():
    response = client.get("/tasks/status/in_progress")
    assert response.status_code == 200
    for task in response.json():
        assert task["status"] == "in_progress"

def test_filter_by_priority():
    response = client.get("/tasks/priority/high")
    assert response.status_code == 200
    for task in response.json():
        assert task["priority"] == "high"