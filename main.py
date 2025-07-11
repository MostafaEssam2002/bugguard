from fastapi import FastAPI
from database import create_db
from routes import tasks
from seed import seed_data 
app = FastAPI()
create_db()
seed_data() 
app.include_router(tasks.router)
"""
1. Root Endpoint ----> GET / - Return API information and available endpoints
"""
@app.get("/")
def root():
    return {"message": "Task Management API", "endpoints": ["/tasks", "/health"]}

"""
2. Health Check ----> GET /health - Return API health status
"""
@app.get("/health")
def health():
    return {"status": "OK"}
