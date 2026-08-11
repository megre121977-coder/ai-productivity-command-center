URGENCY_KEYWORDS = ["urgent", "today", "blocked", "deadline", "decision", "approve", "review"]
RISK_KEYWORDS = ["risk", "delay", "issue", "missing", "unclear", "blocked", "escalate"]
ACTION_KEYWORDS = ["please", "confirm", "send", "review", "prepare", "follow up", "decide"]


def keyword_score(text: str, keywords: list[str]) -> int:
    value = text.lower()
    return sum(1 for keyword in keywords if keyword in value)


def priority_label(score: int) -> str:
    if score >= 5:
        return "High"
    if score >= 2:
        return "Medium"
    return "Low"
