from sqlmodel import SQLModel, create_engine, Session
import os
from dotenv import load_dotenv
sqlite_file_name = "database.db"
engine = create_engine(f"sqlite:///{sqlite_file_name}", echo=True)
def create_db():
    SQLModel.metadata.create_all(engine)
def get_session():
    with Session(engine) as session:
        yield session
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./database.db")
engine = create_engine(DATABASE_URL, echo=True)
