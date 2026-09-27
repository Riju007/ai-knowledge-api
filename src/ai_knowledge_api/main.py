from fastapi import FastAPI
from pydantic import BaseModel, Field, PositiveInt


class HealthResponse(BaseModel):
    health_status: str


class KnowledgeCreate(BaseModel):
    title: str = Field(..., min_length=3)
    content: str = Field(..., min_length=10)
    description: str | None = None


class KnowledgeResponse(BaseModel):
    id: PositiveInt
    title: str
    content: str
    description: str | None = None


knowledge_store: dict[int, KnowledgeResponse] = {}
next_id: int = 1

app = FastAPI()


@app.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    payload: dict[str, str] = {"health_status": "ok"}
    return HealthResponse(**payload)


@app.post("/knowledge")
def knowledge_create(data: KnowledgeCreate) -> KnowledgeResponse:
    global next_id
    knowledge_response = KnowledgeResponse(
        id=next_id, title=data.title, content=data.content, description=data.description
    )
    knowledge_store[next_id] = knowledge_response
    next_id += 1
    return knowledge_response
