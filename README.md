# AI Productivity Command Center

A modern AI-powered productivity dashboard for knowledge workers.

This project helps users turn scattered work inputs into clear priorities, action items, risks, summaries and daily focus plans. It is built as a public-safe portfolio project with synthetic demo data only.

## Why this project exists

Many professionals work across messages, notes, tasks, documents and meetings. The challenge is not having more information. The challenge is knowing what matters, what needs action and what can wait.

AI Productivity Command Center demonstrates how an intelligent assistant could support this workflow without using confidential or company-specific data.

![/dashboard-overview.png

## Core capabilities

- Inbox priority analysis
- Meeting notes summarization
- Task scoring and workload prioritization
- Executive brief generation
- Document Q&A style insights
- Risk and deadline detection
- Clean dashboard UI
- API-first backend

## Demo principles

This repository is intentionally generic:

- No employer references
- No real customer names
- No healthcare references
- No confidential data
- No personal information
- Synthetic examples only

## Tech stack

| Area | Technology |
|---|---|
| Backend | Python, FastAPI, Pydantic |
| Analytics | Pandas, rule-based scoring |
| Frontend | React, Vite, CSS |
| Testing | Pytest |
| DevOps | Docker, GitHub Actions |
| Docs | Case study, architecture, LinkedIn post |

## Repository structure

```text
ai-productivity-command-center/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   └── services/
│   └── tests/
├── data/
├── docs/
├── frontend/
├── scripts/
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

## Quick start

### Run the local demo

```bash
python scripts/run_demo.py
```

### Run the FastAPI backend

```bash
pip install -e .[dev]
uvicorn backend.app.main:app --reload
```

Open the API docs at:

```text
http://127.0.0.1:8000/docs
```

### Run with Docker

```bash
docker compose up --build
```

## Example endpoints

### Analyze inbox items

```bash
curl -X POST http://127.0.0.1:8000/analyze/inbox \
  -H "Content-Type: application/json" \
  -d '{"file_path":"data/sample_inbox.csv"}'
```

### Summarize meeting notes

```bash
curl -X POST http://127.0.0.1:8000/analyze/meeting-notes \
  -H "Content-Type: application/json" \
  -d '{"file_path":"data/sample_meeting_notes.txt"}'
```

### Prioritize tasks

```bash
curl -X POST http://127.0.0.1:8000/analyze/tasks \
  -H "Content-Type: application/json" \
  -d '{"file_path":"data/sample_tasks.csv"}'
```

### Create an executive brief

```bash
curl -X POST http://127.0.0.1:8000/generate/executive-brief \
  -H "Content-Type: application/json" \
  -d '{"topic":"AI adoption for knowledge work","audience":"leadership team","objective":"explain benefits, risks and next steps"}'
```

## Example output

```json
{
  "total_items": 6,
  "high_priority_items": 2,
  "top_theme": "decision needed",
  "recommended_focus": [
    "Reply to high urgency items first",
    "Clarify blockers before starting deep work",
    "Move low urgency updates into a batch review window"
  ]
}
```

## What this project demonstrates

- Ability to structure an AI product idea
- Practical business workflow thinking
- Backend API implementation
- Data processing with Python
- Clean frontend dashboard design
- Responsible public portfolio setup
- Clear documentation and positioning

## Future roadmap

- Add authentication
- Add file upload UI
- Add local vector search for documents
- Add calendar-aware focus planning
- Add optional model provider integration
- Add browser extension prototype

## License

MIT License. See `LICENSE`.
