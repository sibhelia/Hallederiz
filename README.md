# Hallederiz

> **Sen anlat, gerisini Hallederiz.**
> Arızayı anlat, usta gelsin.

Evdeki sorunu anlayan, doğru hizmet alanını belirleyen, uygun ve müsait ustayı bulan, randevuyu yöneten, işin yapıldığını doğrulayan ve iki tarafın memnuniyetini ölçen ev hizmetleri platformu.

Ayrıntılı ürün ve geliştirme planı: [`docs/PLAN.md`](docs/PLAN.md)

## Repo yapısı

```
apps/
  mobile/     Flutter uygulaması (iOS + Android)      — Sprint 1'de oluşturulacak
  web/        Next.js public site                     — Faz 2
  admin/      Next.js admin + HITL paneli             — Sprint 2
backend/      FastAPI (modüler monolit) + AI gateway
ml/           Veri setleri, eğitim, değerlendirme, RAG bilgi tabanı
infra/        docker-compose ve deploy dosyaları
docs/         Plan ve mimari karar kayıtları (ADR)
```

## Teknoloji yığını

Flutter · Next.js + TypeScript · Python + FastAPI · PostgreSQL + PostGIS + pgvector · Redis · Groq (LLM) · OpenStreetMap

## Lokal geliştirme

### Gereksinimler

- Docker Desktop (WSL2 backend)
- Python 3.12+ ve [uv](https://docs.astral.sh/uv/) (ya da pip)
- Git

### 1. Ortam değişkenleri

```bash
cp .env.example .env
# .env içindeki GROQ_API_KEY değerini doldur
```

### 2. Altyapıyı başlat (PostgreSQL + PostGIS + pgvector, Redis)

```bash
docker compose --env-file .env -f infra/docker-compose.yml up -d db redis
```

### 3. Backend'i çalıştır

**Seçenek A — Docker içinde:**

```bash
docker compose --env-file .env -f infra/docker-compose.yml up -d --build backend
```

**Seçenek B — Bilgisayarında (geliştirme için daha hızlı):**

```bash
cd backend
uv sync --extra dev            # veya: python -m venv .venv && pip install -e ".[dev]"
uv run alembic upgrade head
uv run uvicorn app.main:app --reload
```

### 4. Kontrol

- API dokümantasyonu: http://localhost:8000/docs
- Sağlık kontrolü: http://localhost:8000/api/v1/health

### Testler

```bash
cd backend
uv run ruff check .
uv run pytest
```
