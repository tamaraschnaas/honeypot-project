from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from sqlalchemy import create_engine, text
import os
from datetime import datetime

DB_USER = os.getenv("POSTGRES_USER", "honeyuser")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "honeypass")
DB_NAME = os.getenv("POSTGRES_DB", "honeypot")
DB_HOST = os.getenv("POSTGRES_HOST", "db")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

app = FastAPI(title="Honeypot API")

class EventIn(BaseModel):
    event_time: Optional[datetime] = None
    src_ip: Optional[str] = None
    event_type: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    command: Optional[str] = None
    raw_json: Optional[dict] = None

@app.get("/")
def root():
    return {"message": "API funcionando"}

@app.get("/health")
def health():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"status": "ok"}

@app.get("/events")
def get_events(limit: int = 50):
    with engine.connect() as conn:
        rows = conn.execute(text("""
            SELECT id, event_time, src_ip, event_type, username, password, command
            FROM cowrie_events
            ORDER BY id DESC
            LIMIT :limit
        """), {"limit": limit}).mappings().all()
    return {"events": [dict(r) for r in rows]}

@app.post("/events")
def create_event(event: EventIn):
    with engine.begin() as conn:
        conn.execute(text("""
            INSERT INTO cowrie_events (event_time, src_ip, event_type, username, password, command, raw_json)
            VALUES (:event_time, :src_ip, :event_type, :username, :password, :command, CAST(:raw_json AS JSONB))
        """), {
            "event_time": event.event_time,
            "src_ip": event.src_ip,
            "event_type": event.event_type,
            "username": event.username,
            "password": event.password,
            "command": event.command,
            "raw_json": None if event.raw_json is None else str(event.raw_json).replace("'", '"')
        })
    return {"message": "evento insertado"}
