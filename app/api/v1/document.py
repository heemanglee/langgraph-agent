from fastapi import APIRouter, Query

from app.schemas.document import CreateDocumentRequest, CreateDocumentResponse
from app.container import document_service

router = APIRouter(
    prefix="/documents",
)


@router.get("")
def get_document(
    question: str = Query(..., min_length=1),
) -> list[dict]:
    document = document_service.get_document(
        question=question,
    )

    return document


@router.post("")
def create_document(
    reuqest: CreateDocumentRequest,
) -> CreateDocumentResponse:
    answer = document_service.create_document(
        question=reuqest.question,
        llm_answer=reuqest.llm_answer,
    )

    return answer
