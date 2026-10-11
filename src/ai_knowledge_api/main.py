from fastapi import FastAPI, HTTPException, Response, status
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


@app.post(
    "/knowledge", status_code=status.HTTP_201_CREATED, response_model=KnowledgeResponse
)
def knowledge_create(data: KnowledgeCreate) -> KnowledgeResponse:
    global next_id
    knowledge_response = KnowledgeResponse(
        id=next_id, title=data.title, content=data.content, description=data.description
    )
    knowledge_store[next_id] = knowledge_response
    next_id += 1
    return knowledge_response


@app.get("/knowledge", response_model=list[KnowledgeResponse])
def knowledge_list() -> list[KnowledgeResponse]:
    knowledge_items = list(knowledge_store.values())
    return knowledge_items


@app.get("/knowledge/{item_id}", response_model=KnowledgeResponse)
def knowledge_detail(item_id: PositiveInt) -> KnowledgeResponse:
    knowledge_obj = knowledge_store.get(item_id)
    if knowledge_obj is not None:
        return knowledge_obj

    error_message = f"Knowledge item with knowledge id: {item_id} does not exist."
    raise HTTPException(status.HTTP_404_NOT_FOUND, error_message)


@app.delete("/knowledge/{item_id}")
def knowledge_delete(item_id: PositiveInt) -> Response:
    knowledge_obj = knowledge_store.get(item_id)
    if knowledge_obj is not None:
        knowledge_store.pop(item_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    error_message = f"Knowledge item with knowledge id: {item_id} does not exist."
    raise HTTPException(status.HTTP_404_NOT_FOUND, error_message)
