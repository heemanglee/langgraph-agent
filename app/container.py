from app.repositories.document_repository import DocumentRepository
from app.services.document_service import DocumentService
from app.services.question_service import QuestionService
from app.llm.chat_model import get_chat_model

document_repository = DocumentRepository()
document_service = DocumentService(
    document_repository=document_repository,
)

question_service = QuestionService(
    chat_model=get_chat_model(),
)
