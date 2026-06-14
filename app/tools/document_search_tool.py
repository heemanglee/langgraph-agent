from langchain_core.tools import tool

from app.services.document_service import DocumentService
from app.container import document_service


@tool
def document_search(question: str) -> str:
    """
    사용자 질문과 관련된 문서를 검색한다.
    """

    documents = document_service.get_document(
        question=question,
    )

    return "\n\n".join(document["llm_answer"] for document in documents)
