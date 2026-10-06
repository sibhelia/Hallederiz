from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.db import engine
from app.core.logging import setup_logging
from app.core.redis import redis_client


@asynccontextmanager
async def lifespan(_: FastAPI):
    setup_logging()
    yield
    await redis_client.aclose()
    await engine.dispose()


app = FastAPI(
    title="Hallederiz API",
    description="Sen anlat, gerisini Hallederiz.",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.get("/", include_in_schema=False)
async def root() -> dict[str, str]:
    return {"app": settings.app_name, "docs": "/docs"}
