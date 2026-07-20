"""FastAPI application entrypoint for OmniBrain."""

import logging
from logging.handlers import RotatingFileHandler

from fastapi import FastAPI

from app.api.status import router as status_router
from app.api.upload import router as upload_router
from app.config import Settings, get_settings
from app.utils.exceptions import register_exception_handlers


def configure_logging(settings: Settings) -> None:
    """Configure console and file logging."""

    settings.logs_dir.mkdir(parents=True, exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
    file_handler = RotatingFileHandler(
        settings.log_file_path,
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.handlers.clear()
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""

    settings = get_settings()
    configure_logging(settings)

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description=(
            "Backend APIs for uploading PDF documents and preparing them for "
            "future OmniBrain ingestion workflows."
        ),
        contact={"name": "OmniBrain Engineering"},
    )

    register_exception_handlers(app)
    app.include_router(upload_router)
    app.include_router(status_router)

    return app


app = create_app()

