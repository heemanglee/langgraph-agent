from pydantic import BaseModel


class CreateDocumentRequest(BaseModel):
    question: str
    llm_answer: str


class CreateDocumentResponse(BaseModel):
    document_id: str
