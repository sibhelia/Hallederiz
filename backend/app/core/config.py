from functools import lru_cache
from pathlib import Path

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

# Repo kökündeki .env dosyası (backend/ klasöründen çalıştırınca da bulunur)
ROOT_ENV = Path(__file__).resolve().parents[3] / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(ROOT_ENV, ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Genel
    app_env: str = "development"
    app_name: str = "Hallederiz"
    log_level: str = "INFO"

    # PostgreSQL
    postgres_user: str = "hallederiz"
    postgres_password: str = "hallederiz_dev"
    postgres_db: str = "hallederiz"
    postgres_host: str = "localhost"
    postgres_port: int = 5432

    # Redis
    redis_url: str = "redis://localhost:6379/0"

    # Dosya depolama (S3 uyumlu)
    s3_endpoint_url: str = "http://localhost:9000"
    s3_access_key: str = "hallederiz"
    s3_secret_key: str = "hallederiz_dev_secret"
    s3_bucket: str = "hallederiz-uploads"

    # Güvenlik
    jwt_secret: str = "change-me-in-production"

    # AI
    llm_provider: str = "groq"
    groq_api_key: str = ""
    groq_model: str = "llama-3.3-70b-versatile"

    # CORS — virgülle ayrılmış liste
    cors_origins: str = "http://localhost:3000,http://localhost:3001"

    @computed_field  # type: ignore[prop-decorator]
    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    @property
    def cors_origin_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]

    @property
    def is_production(self) -> bool:
        return self.app_env == "production"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
