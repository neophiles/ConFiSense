from sqlmodel import SQLModel
from app.db.session import engine


def init_db():
    """
    Initialize the database by creating all tables defined in SQLModel models
    """
    SQLModel.metadata.create_all(engine)