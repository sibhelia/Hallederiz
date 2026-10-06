import logging
from typing import Literal

from fastapi import APIRouter, Response, status
from pydantic import BaseModel
from sqlalchemy import text

from app.core.config import settings
from app.core.db import SessionDep
from app.core.redis import redis_client

logger = logging.getLogger(__name__)
router = APIRouter(tags=["health"])

CheckStatus = Literal["ok", "error"]


class HealthResponse(BaseModel):
    status: CheckStatus
    app: str
    env: str
    checks: dict[str, CheckStatus]
    extensions: list[str] = []


REQUIRED_EXTENSIONS = ("postgis", "vector")


@router.get("/health", response_model=HealthResponse)
async def health(response: Response, session: SessionDep) -> HealthResponse:
    """Veritabanı ve Redis bağlantısını kontrol eder."""
    checks: dict[str, CheckStatus] = {}
    extensions: list[str] = []

    try:
        await session.execute(text("SELECT 1"))
        result = await session.execute(text("SELECT extname FROM pg_extension ORDER BY extname"))
        extensions = [row[0] for row in result]
        missing = [e for e in REQUIRED_EXTENSIONS if e not in extensions]
        checks["database"] = "ok"
        checks["extensions"] = "error" if missing else "ok"
    except Exception:
        logger.exception("Veritabanı sağlık kontrolü başarısız")
        checks["database"] = "error"

    try:
        await redis_client.ping()
        checks["redis"] = "ok"
    except Exception:
        logger.exception("Redis sağlık kontrolü başarısız")
        checks["redis"] = "error"

    overall: CheckStatus = "ok" if all(v == "ok" for v in checks.values()) else "error"
    if overall == "error":
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

    return HealthResponse(
        status=overall,
        app=settings.app_name,
        env=settings.app_env,
        checks=checks,
        extensions=extensions,
    )
