# PostgreSQL 16 + PostGIS 3 + pgvector tek imajda.
# postgis/postgis imajı resmi postgres imajını temel alır ve PGDG apt deposu
# zaten tanımlıdır; pgvector'ü oradan kuruyoruz.
FROM postgis/postgis:16-3.4

RUN apt-get update \
    && apt-get install -y --no-install-recommends postgresql-16-pgvector \
    && rm -rf /var/lib/apt/lists/*

COPY init/ /docker-entrypoint-initdb.d/
