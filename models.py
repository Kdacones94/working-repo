from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class WorkoutLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    exercise_name: str
    sets: int
    reps: int
    weight: float  # Weight used in the exercise
    timestamp: datetime = Field(default_factory=datetime.utcnow)