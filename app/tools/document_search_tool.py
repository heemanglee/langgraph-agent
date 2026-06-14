from langchain_core.tools import tool

from app.services.document_service import DocumentService


class DocumentSearchTool:
    def __init__(self, document_service: DocumentService):
        self.document_service = document_service

    def as_tool(self):
        @tool
        def document_search(question: str) -> str:
            """
            사용자 질문과 관련된 문서를 검색한다.
            """

            documents = self.document_service.get_document(
                question=question,
            )

            return "\n\n".join(document["llm_answer"] for document in documents)

        return document_search
