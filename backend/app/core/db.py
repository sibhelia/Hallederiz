from collections.abc import AsyncIterator
from datetime import datetime
from typing import Annotated
from uuid import UUID, uuid4

from fastapi import Depends
from sqlalchemy import DateTime, func
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app.core.config import settings

engine = create_async_engine(settings.database_url, pool_pre_ping=True)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    """Tüm modellerin temel sınıfı."""


class TimestampedBase(Base):
    """id (uuid) + created_at + updated_at alanlarını ekler (planın 12. bölümündeki kural)."""

    __abstract__ = True

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )


async def get_session() -> AsyncIterator[AsyncSession]:
    """FastAPI dependency: istek başına bir veritabanı oturumu."""
    async with SessionLocal() as session:
        yield session


# Endpoint'lerde kullanım:  async def handler(session: SessionDep): ...
SessionDep = Annotated[AsyncSession, Depends(get_session)]
