
# Campus Scheduler (Starter)

A minimal FastAPI + SQLAlchemy starter for a role-based campus course scheduler.

## Features (MVP)
- User signup & login
- JWT authentication
- Role-based access (`student`, `instructor`, `admin`)
- SQLite database (dev)

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # then edit values
uvicorn app.main:app --reload
```

## Environment
Create `.env` based on `.env.example`.

## Run tests
```bash
pytest -q
```

## Next Sprints
- Add models for Rooms, Courses, Sections, Meetings
- Conflict detection (room/time, instructor double-booking)
- Student schedule view, approvals, audit log

Generated on 2025-11-28T01:24:36.964325Z
![CI](https://github.com/Tashanatsok/campus-scheduler/actions/workflows/ci.yml/badge.svg)
