from typing import Optional, Any
from pydantic import BaseModel

from beanie import Document

class GeneralProgramming(Document):
    question: str
    answer: str
    keywords: list[str]
    difficulty: str
    level: str


class Response(BaseModel):
    status_code: int
    data: Optional[Any]
