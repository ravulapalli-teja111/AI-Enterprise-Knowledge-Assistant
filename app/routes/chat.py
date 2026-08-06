from fastapi import APIRouter
from app.models.chat_model import ChatRequest
from app.services.openai_service import ask_ai

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest):
    answer = ask_ai(request.question)

    return {
        "question": request.question,
        "answer": answer
    }