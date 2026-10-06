"""Sağlık kontrolü testleri.

Bu testler çalışan bir PostgreSQL ve Redis bekler:
    docker compose --env-file .env -f infra/docker-compose.yml up -d db redis
"""
from httpx import ASGITransport, AsyncClient

from app.main import app


async def test_root():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        resp = await client.get("/")
    assert resp.status_code == 200
    assert resp.json()["app"] == "Hallederiz"


async def test_health_ok():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        resp = await client.get("/api/v1/health")
    body = resp.json()
    assert resp.status_code == 200, body
    assert body["status"] == "ok"
    assert body["checks"] == {"database": "ok", "extensions": "ok", "redis": "ok"}
    assert {"postgis", "vector"} <= set(body["extensions"])
