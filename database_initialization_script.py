import os
from sqlmodel import SQLModel, create_engine


# Load database names from environment variables or use defaults
DATABASES = os.getenv("DATABASES", "workout_log.db,backup_workout_log.db").split(",")

# Define database directory (sibling to 'app' directory)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Current directory
DB_DIR = os.path.join(BASE_DIR, "..", "database")  # Sibling 'database' directory

# Ensure the database directory exists
os.makedirs(DB_DIR, exist_ok=True)

# Create database engine dictionary
ENGINES = {
    db_name: create_engine(f"sqlite:///{os.path.join(DB_DIR, db_name.strip())}", echo=True)
    for db_name in DATABASES
}

def initialize_databases():
    """Creates database files and initializes tables."""
    for name, engine in ENGINES.items():
        print(f"Creating database: {name} at {engine.url}")
        SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    initialize_databases()
    print("Database initialization complete.")