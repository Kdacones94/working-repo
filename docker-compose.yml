version: "3.9"

services:
  workout-api:
    build: .
    container_name: workout-api
    restart: always
    ports:
      - "8000:8000"
    environment:
      - DATABASES=workout_log.db,backup_workout_log.db
      - LOG_LEVEL=info
      - LOG_FILE=/logs/app.log
    volumes:
      - workout_db:/database  # Named volume for database persistence
      - workout_logs:/logs  # Named volume for logs
    command: ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

volumes:
  workout_db:
    name: workout_db
  workout_logs:
    name: workout_logs