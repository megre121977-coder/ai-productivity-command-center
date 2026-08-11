import pandas as pd
from datetime import datetime
from backend.app.services.scoring import priority_label


def prioritize_tasks(df: pd.DataFrame) -> dict:
    df = df.rename(columns={c: c.lower() for c in df.columns}).copy()
    required = {"task", "importance", "effort", "due_date"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    today = datetime.today().date()
    df["due"] = pd.to_datetime(df["due_date"], errors="coerce").dt.date
    df["days_until_due"] = df["due"].apply(lambda d: 999 if pd.isna(d) else (d - today).days)
    df["urgency_points"] = df["days_until_due"].apply(lambda d: 3 if d <= 1 else 2 if d <= 3 else 1 if d <= 7 else 0)
    df["focus_score"] = df["importance"] * 2 + df["urgency_points"] - df["effort"].clip(lower=0, upper=5) * 0.5
    df["priority"] = df["focus_score"].round().astype(int).apply(priority_label)

    ordered = df.sort_values("focus_score", ascending=False)[
        ["task", "importance", "effort", "due_date", "priority", "focus_score"]
    ].to_dict(orient="records")

    return {
        "total_tasks": int(len(df)),
        "focus_plan": ordered[:5],
        "recommendations": [
            "Start with high importance tasks that are due soon.",
            "Reduce or delegate low impact, high effort tasks where possible.",
            "Reserve deep work time for the highest focus score item."
        ],
    }
