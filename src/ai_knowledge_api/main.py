from fastapi import FastAPI
from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    health_status: str


class KnowledgeCreate(BaseModel):
    title: str = Field(..., min_length=3)
    content: str = Field(..., min_length=10)


app = FastAPI()


@app.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    payload: dict[str, str] = {"health_status": "ok"}
    return HealthResponse(**payload)


@app.post("/knowledge")
def knowledge_create(data: KnowledgeCreate) -> KnowledgeCreate:
    return data
