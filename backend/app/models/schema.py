from pydantic import BaseModel

class QueryRequest(BaseModel):
    question: str
    program: str


class QueryResponse(BaseModel):
    answer: str
    sources: list

