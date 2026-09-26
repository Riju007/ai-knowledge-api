from fastapi import FastAPI
from pydantic import BaseModel


class HealthResponse(BaseModel):
    health_status: str


class KnowledgeCreate(BaseModel):
    title: str
    content: str


app = FastAPI()


@app.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    payload: dict[str, str] = {"health_status": "ok"}
    return HealthResponse(**payload)


@app.post("/knowledge")
def knowledge_create(data: KnowledgeCreate) -> KnowledgeCreate:
    return data
