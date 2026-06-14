from fastapi import APIRouter, Depends

from app.dependencies import get_agent
from app.schemas.question import AskQuestionRequest, AskQuestionResponse

router = APIRouter(
    prefix="/questions",
)


@router.post("")
def ask_question(
    request: AskQuestionRequest,
    agent=Depends(get_agent),
) -> AskQuestionResponse:
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

    return AskQuestionResponse(
        question=request.question,
        llm_answer=response["messages"][-1].content,
    )
