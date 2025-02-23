from sqlmodel import create_engine, Session
from contextlib import contextmanager

# Dictionary to store multiple database connections
DATABASES = {
    "default": "sqlite:///workout_log.db",
    "backup": "sqlite:///backup_workout_log.db"
}

# Store database engines
ENGINES = {name: create_engine(url, echo=True) for name, url in DATABASES.items()}

@contextmanager
def get_session(db_name: str = "default"):
    """Session generator that creates and manages database sessions."""
    if db_name not in ENGINES:
        raise ValueError(f"Database '{db_name}' not found in configuration.")
    
    session = Session(ENGINES[db_name])
    try:
        yield session  # Provide session to caller
        session.commit()  # Commit transaction if successful
    except Exception as e:
        session.rollback()  # Rollback on error
        raise e
    finally:
        session.close()  # Ensure session cleanup
        
from sqlmodel import SQLModel

def initialize_databases():
    """Create tables for all configured databases."""
    for engine in ENGINES.values():
        SQLModel.metadata.create_all(engine)