-- Veritabanı ilk oluşturulduğunda bir kez çalışır.
-- Aynı eklentiler Alembic'in ilk migration'ında da IF NOT EXISTS ile oluşturulur;
-- bu dosya sadece temiz bir kurulumda hazır olmalarını garanti eder.
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE EXTENSION IF NOT EXISTS unaccent;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
