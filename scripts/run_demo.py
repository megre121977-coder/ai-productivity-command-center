from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from backend.app.data_loader import load_csv, load_text
from backend.app.services.inbox import analyze_inbox
from backend.app.services.tasks import prioritize_tasks
from backend.app.services.meeting_notes import summarize_meeting_notes
from backend.app.services.executive_brief import generate_executive_brief
from backend.app.services.document_chat import answer_document_question


def section(title, data):
    print()
    print("=" * 80)
    print(title)
    print("=" * 80)
    print(data)


if __name__ == "__main__":
    section("Inbox Analysis", analyze_inbox(load_csv("data/sample_inbox.csv")))
    section("Task Prioritization", prioritize_tasks(load_csv("data/sample_tasks.csv")))
    section("Meeting Notes", summarize_meeting_notes(load_text("data/sample_meeting_notes.txt")))
    section("Executive Brief", generate_executive_brief("AI productivity workflows", "leadership team", "identify practical use cases and next steps"))
    section("Document Q&A", answer_document_question(load_text("data/sample_document.txt"), "What are the risks?"))
