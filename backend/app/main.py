from fastapi import FastAPI, HTTPException
from backend.app.models import FileRequest, ExecutiveBriefRequest, DocumentQuestionRequest
from backend.app.data_loader import load_csv, load_text
from backend.app.services.inbox import analyze_inbox
from backend.app.services.tasks import prioritize_tasks
from backend.app.services.meeting_notes import summarize_meeting_notes
from backend.app.services.executive_brief import generate_executive_brief
from backend.app.services.document_chat import answer_document_question

app = FastAPI(
    title="AI Productivity Command Center",
    description="A public-safe AI productivity assistant for prioritization, summaries and executive briefs.",
    version="0.1.0",
)

@app.get("/")
def root():
    return {"message": "AI Productivity Command Center API", "status": "ready"}

@app.post("/analyze/inbox")
def inbox_endpoint(request: FileRequest):
    try:
        return analyze_inbox(load_csv(request.file_path))
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

@app.post("/analyze/tasks")
def tasks_endpoint(request: FileRequest):
    try:
        return prioritize_tasks(load_csv(request.file_path))
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

@app.post("/analyze/meeting-notes")
def meeting_notes_endpoint(request: FileRequest):
    try:
        return summarize_meeting_notes(load_text(request.file_path))
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

@app.post("/generate/executive-brief")
def executive_brief_endpoint(request: ExecutiveBriefRequest):
    return generate_executive_brief(request.topic, request.audience, request.objective)

@app.post("/document/question")
def document_question_endpoint(request: DocumentQuestionRequest):
    try:
        return answer_document_question(load_text(request.file_path), request.question)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
