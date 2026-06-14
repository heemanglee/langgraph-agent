from pydantic import BaseModel, Field


class AskQuestionRequest(BaseModel):
    question: str = Field(..., min_lenth=1)


class AskQuestionResponse(BaseModel):
    question: str
    llm_answer: str
