from backend.app.services.scoring import ACTION_KEYWORDS, RISK_KEYWORDS


def summarize_meeting_notes(text: str) -> dict:
    lines = [line.strip(" -") for line in text.splitlines() if line.strip()]
    actions = [line for line in lines if any(k in line.lower() for k in ACTION_KEYWORDS)]
    risks = [line for line in lines if any(k in line.lower() for k in RISK_KEYWORDS)]
    decisions = [line for line in lines if "decision" in line.lower() or "decided" in line.lower()]

    return {
        "summary": "Meeting notes reviewed and structured into decisions, actions and risks.",
        "decisions": decisions[:10],
        "action_items": actions[:10],
        "risks": risks[:10],
        "next_best_action": "Confirm owners and deadlines for all open action items.",
    }
