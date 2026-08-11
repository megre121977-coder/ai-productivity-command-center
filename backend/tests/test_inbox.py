import pandas as pd
from backend.app.services.inbox import analyze_inbox


def test_inbox_detects_high_priority_item():
    df = pd.DataFrame({
        "subject": ["Decision needed today", "Weekly update"],
        "sender": ["A", "B"],
        "body": ["Please review and approve. This is urgent.", "Routine note."],
    })
    result = analyze_inbox(df)
    assert result["total_items"] == 2
    assert result["high_priority_items"] >= 1
