from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from opensearchpy import OpenSearch

from app.repositories.document_repository import DocumentRepository
from app.services.document_service import DocumentService
from app.services.question_service import QuestionService
from app.core.config import settings
from app.tools.document_search_tool import DocumentSearchTool

opensearch_client = OpenSearch(
    hosts=[
        {
            "host": settings.OPENSEARCH_HOST,
            "port": settings.OPENSEARCH_PORT,
            "scheme": "https" if settings.OPENSEARCH_USE_SSL else "http",
        }
    ],
    use_ssl=settings.OPENSEARCH_USE_SSL,
    verify_certs=settings.OPENSEARCH_VERIFY_CERTS,
    timeout=5,
)

llm = ChatOpenAI(
    api_key=settings.OPENAI_API_KEY,
    model=settings.OPENAI_CHAT_MODEL,
    temperature=0,
)

question_service = QuestionService(
    llm=llm,
)


document_service = DocumentService(
    document_repository=DocumentRepository(
        opensearch_client=opensearch_client,
    ),
)

document_search_tool = DocumentSearchTool(
    document_service=document_service,
).as_tool()

agent = create_agent(
    model=llm,
    tools=[
        document_search_tool,
    ],
)
