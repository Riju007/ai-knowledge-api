from fastapi import FastAPI
from fastapi import status

app = FastAPI()


@app.get("/health")
def health_check() -> dict:
    payload: dict[str, int] = {"health_status": "ok"}
    return payload
