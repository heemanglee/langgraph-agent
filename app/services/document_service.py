from datetime import datetime, timezone

from app.repositories.document_repository import DocumentRepository
from app.schemas.document import CreateDocumentResponse


class DocumentService:
    def __init__(self, document_repository: DocumentRepository):
        self.document_repository = document_repository

    def get_document(self, question: str) -> list[dict]:
        documents: list[dict] = self.document_repository.get_documents(
            question=question,
        )

        return documents

    def create_document(self, question: str, llm_answer: str) -> CreateDocumentResponse:
        document_id = self.document_repository.create_document(
            question=question,
            llm_answer=llm_answer,
            created_at=datetime.now(timezone.utc).isoformat(),
        )

        return CreateDocumentResponse(document_id=document_id)
