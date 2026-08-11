from backend.app.services.scoring import ACTION_KEYWORDS, RISK_KEYWORDS


def answer_document_question(text: str, question: str) -> dict:
    question_lower = question.lower()
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    if "risk" in question_lower:
        matches = [line for line in lines if any(k in line.lower() for k in RISK_KEYWORDS)]
        answer_type = "risk-focused answer"
    elif "action" in question_lower or "todo" in question_lower:
        matches = [line for line in lines if any(k in line.lower() for k in ACTION_KEYWORDS)]
        answer_type = "action-focused answer"
    else:
        matches = lines[:5]
        answer_type = "general summary answer"

    return {
        "question": question,
        "answer_type": answer_type,
        "answer": matches[:10],
        "note": "This is a local rule-based demo. Future versions can connect to a model provider."
    }
