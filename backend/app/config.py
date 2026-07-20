"""Application configuration loaded from environment variables."""

from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime settings for the OmniBrain backend."""

    app_name: str = "OmniBrain Backend"
    app_version: str = "1.0.0"
    environment: str = "development"
    max_upload_size_mb: int = Field(default=100, gt=0)
    allowed_mime_types: set[str] = {"application/pdf"}
    uploads_dir: Path = Path("app/uploads")
    logs_dir: Path = Path("app/logs")
    log_file_name: str = "backend.log"
    ingestion_delay_seconds: float = Field(default=2.0, ge=0)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def max_upload_size_bytes(self) -> int:
        """Return the maximum upload size in bytes."""

        return self.max_upload_size_mb * 1024 * 1024

    @property
    def log_file_path(self) -> Path:
        """Return the application log file path."""

        return self.logs_dir / self.log_file_name


@lru_cache
def get_settings() -> Settings:
    """Return cached application settings."""

    return Settings()

