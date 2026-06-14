from fastapi import APIRouter, Depends, Query

from app.dependencies import get_document_service
from app.schemas.document import CreateDocumentRequest, CreateDocumentResponse
from app.services.document_service import DocumentService

router = APIRouter(
    prefix="/documents",
)


@router.get("")
def get_document(
    question: str = Query(..., min_length=1),
    document_service: DocumentService = Depends(get_document_service),
) -> list[dict]:
    document = document_service.get_document(
        question=question,
    )

    return document


@router.post("")
def create_document(
    reuqest: CreateDocumentRequest,
    document_service: DocumentService = Depends(get_document_service),
) -> CreateDocumentResponse:
    answer = document_service.create_document(
        question=reuqest.question,
        llm_answer=reuqest.llm_answer,
    )

    return answer
