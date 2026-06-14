from langchain.agents import create_agent

from app.llm.chat_model import get_chat_model
from app.tools.document_search_tool import document_search

agent = create_agent(
    model=get_chat_model(),
    tools=[
        document_search,
    ],
)
