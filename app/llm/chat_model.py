from langchain_openai import ChatOpenAI

from app.core.config import settings


def get_chat_model() -> ChatOpenAI:
    return ChatOpenAI(
        api_key=settings.OPENAI_API_KEY,
        model=settings.OPENAI_CHAT_MODEL,
        temperature=0,
    )
