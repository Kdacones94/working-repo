from fastapi import FastAPI
from sqlmodel import Session, select
from database import engine, WorkoutLog

app = FastAPI()

@app.post("/workouts/")
def create_workout(workout: WorkoutLog):
    with Session(engine) as session:
        session.add(workout)
        session.commit()
        session.refresh(workout)
        return workout

@app.get("/workouts/")
def get_workouts():
    with Session(engine) as session:
        workouts = session.exec(select(WorkoutLog)).all()
        return workouts