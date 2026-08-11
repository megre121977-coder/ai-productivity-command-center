import pandas as pd
from backend.app.services.scoring import URGENCY_KEYWORDS, RISK_KEYWORDS, ACTION_KEYWORDS, keyword_score, priority_label


def analyze_inbox(df: pd.DataFrame) -> dict:
    df = df.rename(columns={c: c.lower() for c in df.columns}).copy()
    required = {"subject", "sender", "body"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    text = (df["subject"].fillna("") + " " + df["body"].fillna("")).astype(str)
    df["urgency_score"] = text.apply(lambda x: keyword_score(x, URGENCY_KEYWORDS))
    df["risk_score"] = text.apply(lambda x: keyword_score(x, RISK_KEYWORDS))
    df["action_score"] = text.apply(lambda x: keyword_score(x, ACTION_KEYWORDS))
    df["priority_score"] = df["urgency_score"] * 2 + df["risk_score"] + df["action_score"]
    df["priority"] = df["priority_score"].apply(priority_label)

    top_items = df.sort_values("priority_score", ascending=False).head(5)[
        ["subject", "sender", "priority", "priority_score"]
    ].to_dict(orient="records")

    return {
        "total_items": int(len(df)),
        "high_priority_items": int((df["priority"] == "High").sum()),
        "medium_priority_items": int((df["priority"] == "Medium").sum()),
        "low_priority_items": int((df["priority"] == "Low").sum()),
        "top_items": top_items,
        "recommended_focus": [
            "Handle high priority items before routine updates.",
            "Clarify blockers and decision requests first.",
            "Batch low priority messages into one review window."
        ],
    }
