"""PostgreSQL eklentileri: postgis, vector, pg_trgm, unaccent

Revision ID: 0001
Revises:
Create Date: 2026-10-03
"""
from collections.abc import Sequence

from alembic import op

revision: str = "0001"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

EXTENSIONS = ("postgis", "vector", "pg_trgm", "unaccent")


def upgrade() -> None:
    for ext in EXTENSIONS:
        op.execute(f'CREATE EXTENSION IF NOT EXISTS "{ext}"')


def downgrade() -> None:
    # Eklentileri bilinçli olarak kaldırmıyoruz; başka nesneler onlara bağlı olabilir.
    pass
