from fastapi import FastAPI
from app.routes.chat import router as chat_router

app = FastAPI(
    title="AI Enterprise Knowledge Assistant",
    version="1.0"
)

app.include_router(chat_router)

@app.get("/")
def home():
    return {
        "message": "AI Enterprise Knowledge Assistant"
    }