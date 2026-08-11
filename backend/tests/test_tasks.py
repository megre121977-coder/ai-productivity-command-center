import pandas as pd
from datetime import date, timedelta
from backend.app.services.tasks import prioritize_tasks


def test_tasks_returns_focus_plan():
    df = pd.DataFrame({
        "task": ["Prepare brief", "Clean notes"],
        "importance": [5, 2],
        "effort": [2, 1],
        "due_date": [str(date.today() + timedelta(days=1)), str(date.today() + timedelta(days=10))],
    })
    result = prioritize_tasks(df)
    assert result["total_tasks"] == 2
    assert result["focus_plan"][0]["task"] == "Prepare brief"
