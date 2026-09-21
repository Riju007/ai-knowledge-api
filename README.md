# AI Knowledge API

A small, production-style Python backend built incrementally while learning the modern Python ecosystem.

## Goal

Build a clean FastAPI service for storing and exposing knowledge items, then evolve it into an AI/GenAI backend.

The project is intentionally small. Each new capability is introduced only when the underlying concept has been learned and tested.

## Learning stack

- Python 3.12+
- uv
- FastAPI
- Pydantic
- pytest
- Ruff
- ty
- Docker
- GitHub Actions
- Git/GitHub

## Planned evolution

```text
Python foundation
    ↓
FastAPI + Pydantic
    ↓
pytest + Ruff + ty
    ↓
configuration
    ↓
PostgreSQL + SQLAlchemy
    ↓
Docker
    ↓
GitHub Actions
    ↓
embeddings + vector search
    ↓
RAG + LLM
    ↓
local AI
    ↓
agents / MCP
```

## Learning principle

> Learn → implement → test → inspect → improve → move forward.

## Current status

Phase 0 — Project foundation

- [ ] Initialize project with `uv`
- [ ] Understand `pyproject.toml`
- [ ] Create and understand `uv.lock`
- [ ] Verify the virtual environment workflow
- [ ] Add FastAPI and Pydantic
- [ ] Add pytest, Ruff and ty as development tooling
- [ ] Make the first small API endpoint
- [ ] Add the first test
- [ ] Run linting, formatting and type checking

## Development philosophy

Keep the code small, readable, typed, tested and reproducible.

Avoid introducing databases, Docker, vector stores or LLMs before the API foundation is solid.
