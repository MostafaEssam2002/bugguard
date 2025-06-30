from sqlmodel import Session, select
from database import engine
from models import Task, TaskStatus, TaskPriority
from datetime import datetime, timedelta, timezone
import random

def seed_data():
    with Session(engine) as session:
        if session.exec(select(Task)).first():  
            return
        priorities = list(TaskPriority)
        statuses = list(TaskStatus)
        tasks = []
        for i in range(1, 101):
            task = Task(
                title=f"Seed Task {i}",
                description=f"This is the description for task {i}",
                status=random.choice(statuses),
                priority=random.choice(priorities),
                due_date=datetime.now(timezone.utc) + timedelta(days=random.randint(1, 30)),
                assigned_to=random.choice(["Alice", "Bob", "Charlie", "Dana", "medo"]) or None
            )
            tasks.append(task)
        session.add_all(tasks)
        session.commit()
        print("####################################################")
        print(len(tasks))
        print("####################################################")
