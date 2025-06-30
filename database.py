from sqlmodel import SQLModel, create_engine, Session
import os
from dotenv import load_dotenv
# Load environment variables
load_dotenv()
# Get database URL from .env or use default
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./database.db")
# Create a single engine instance
engine = create_engine(DATABASE_URL, echo=True)
# Create tables
def create_db():
    SQLModel.metadata.create_all(engine)
# Dependency to get DB session
def get_session():
    with Session(engine) as session:
        yield session