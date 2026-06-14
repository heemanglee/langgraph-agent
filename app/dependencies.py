from app.container import (
    agent,
    llm,
    document_service,
    question_service,
)


def get_document_service():
    return document_service


def get_question_service():
    return question_service


def get_agent():
    return agent


def get_chat_model():
    return llm
