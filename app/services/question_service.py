from app.schemas.question import AskQuestionResponse
from langchain_openai import ChatOpenAI


class QuestionService:
    def __init__(self, chat_model: ChatOpenAI):
        self.llm = chat_model

    def ask(self, question: str) -> AskQuestionResponse:
        response = self.llm.invoke(
            input=question,
        )

        return AskQuestionResponse(
            question=question,
            llm_answer=response.content,
        )
