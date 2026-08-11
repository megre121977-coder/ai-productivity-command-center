from pydantic import BaseModel
from typing import Optional

class FileRequest(BaseModel):
    file_path: str

class ExecutiveBriefRequest(BaseModel):
    topic: str
    audience: str = "general business audience"
    objective: Optional[str] = None

class DocumentQuestionRequest(BaseModel):
    file_path: str
    question: str
