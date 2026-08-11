from datetime import date


def generate_executive_brief(topic: str, audience: str, objective: str | None = None) -> dict:
    objective_text = objective or "provide a concise overview and recommended next steps"
    return {
        "title": f"Executive Brief: {topic}",
        "date": str(date.today()),
        "audience": audience,
        "objective": objective_text,
        "executive_summary": (
            f"This brief explains {topic} for {audience}. The goal is to {objective_text}. "
            "It highlights value, risks, decisions needed and practical next steps."
        ),
        "key_points": [
            "Clarify the business problem before selecting a tool or workflow.",
            "Focus on repeatable tasks where automation can save time or reduce manual errors.",
            "Keep human review in the loop for decisions with business impact."
        ],
        "risks": [
            "Poor input quality can lead to poor output quality.",
            "Unclear ownership can slow adoption.",
            "Sensitive data requires appropriate governance before use."
        ],
        "recommended_next_steps": [
            "Select one practical pilot use case.",
            "Define success criteria and expected output format.",
            "Test with synthetic or non-sensitive data first."
        ],
    }
