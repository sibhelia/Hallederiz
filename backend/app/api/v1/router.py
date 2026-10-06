from fastapi import APIRouter

from app.modules.health.router import router as health_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(health_router)

# Sonraki sprintlerde eklenecek modüller:
# auth, users, providers, catalog, requests, dispatch, appointments,
# jobs, reviews, trust, homes, chat, notifications, admin, ai
