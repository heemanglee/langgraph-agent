from fastapi import FastAPI
from app.core.config import settings

app = FastAPI()


@app.get("/health")
def read_root():
    return {"app_env": settings.app_env, "health": "ok"}
