from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.config import settings
from app.core.opensearch import opensearch_client
from app.api.v1.question import router as question_router
from app.api.v1.document import router as document_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        info = opensearch_client.info()
        print(
            f"OpenSearch Connected: {info['version']['distribution']} "
            f"{info['version']['number']}"
        )
    except Exception as e:
        raise RuntimeError(f"OpenSearch connection failed: {e}")

    yield


app = FastAPI(
    lifespan=lifespan,
)
app.include_router(
    question_router,
    prefix="/api/v1",
    tags=["questions"],
)
app.include_router(
    document_router,
    prefix="/api/v1",
    tags=["documents"],
)
