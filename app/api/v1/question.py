from fastapi import APIRouter, Query

from app.services.question_service import QuestionService
from app.schemas.question import AskQuestionRequest, AskQuestionResponse
from app.services.document_service import DocumentService
from app.agent.react_agent import agent

router = APIRouter(
    prefix="/questions",
)


@router.post("")
def ask_question(request: AskQuestionRequest):
    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": request.question,
                }
            ]
        }
    )

    return {"answer": response["messages"][-1].content}
