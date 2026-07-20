"""File storage service for uploaded PDFs."""

import logging
import re
from pathlib import Path
from uuid import uuid4

import aiofiles
from fastapi import UploadFile

from app.config import Settings
from app.models.response_models import ProcessingStatus, UploadResponse
from app.services.ingestion_service import queue_document
from app.utils.validators import validate_pdf_upload

logger = logging.getLogger(__name__)

SAFE_FILENAME_PATTERN = re.compile(r"[^A-Za-z0-9_.-]+")


def sanitize_filename(filename: str) -> str:
    """Return a filesystem-safe filename while preserving readability."""

    original_name = Path(filename).name
    sanitized = SAFE_FILENAME_PATTERN.sub("_", original_name).strip("._")
    return sanitized or "document.pdf"


def build_secure_filename(original_filename: str) -> str:
    """Generate a UUID-prefixed filename that will not overwrite existing files."""

    safe_name = sanitize_filename(original_filename)
    return f"{uuid4().hex}_{safe_name}"


async def save_pdf_upload(file: UploadFile, settings: Settings) -> UploadResponse:
    """Validate and persist a PDF upload, then create its initial status."""

    content = await validate_pdf_upload(file, settings)
    settings.uploads_dir.mkdir(parents=True, exist_ok=True)

    document_id = str(uuid4())
    secure_filename = build_secure_filename(file.filename or "document.pdf")
    destination = settings.uploads_dir / secure_filename

    while destination.exists():
        secure_filename = build_secure_filename(file.filename or "document.pdf")
        destination = settings.uploads_dir / secure_filename

    async with aiofiles.open(destination, "wb") as output_file:
        await output_file.write(content)

    queue_document(document_id)
    logger.info("Uploaded PDF saved: document_id=%s filename=%s", document_id, secure_filename)

    return UploadResponse(
        document_id=document_id,
        filename=secure_filename,
        status=ProcessingStatus.PROCESSING,
        message="Upload successful",
    )

