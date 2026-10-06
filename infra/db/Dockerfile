# PostgreSQL 16 + PostGIS 3 + pgvector tek imajda.
# Resmi postgres imajında PostgreSQL'in kendi apt deposu (PGDG) tanımlı;
# PostGIS ve pgvector'ü oradan kuruyoruz. "bookworm" = Debian 12.
FROM postgres:16-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    postgresql-16-postgis-3 \
    postgresql-16-postgis-3-scripts \
    postgresql-16-pgvector \
    && rm -rf /var/lib/apt/lists/*

COPY init/ /docker-entrypoint-initdb.d/