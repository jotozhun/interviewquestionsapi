from typing import Optional, Any
from pydantic import BaseModel

from beanie import Document

class GeneralProgramming(Document):
    question: str
    answer: str
    keywords: list[str]
    difficulty: str
    level: str
    tags: list[str]


class Testing(GeneralProgramming):
    tools: list[str]


class Mobile(GeneralProgramming):
    tools: list[str]


class Frontend(GeneralProgramming):
    tools: list[str]


class Backend(GeneralProgramming):
    tools: list[str]


class DevOps(GeneralProgramming):
    tools: list[str]


class DataScience(GeneralProgramming):
    tools: list[str]


class DataEngineer(GeneralProgramming):
    tools: list[str]


class Databases(GeneralProgramming):
    tools: list[str]


class CloudArchitect(GeneralProgramming):
    tools: list[str]


class ArtificialIntelligence(GeneralProgramming):
    tools: list[str]


class Response(BaseModel):
    status_code: int
    data: Optional[Any]


theoric_programming_models = [GeneralProgramming, Testing, Mobile, Frontend,
                              Backend, DevOps, DataScience, DataEngineer,
                              Databases, CloudArchitect, ArtificialIntelligence]
