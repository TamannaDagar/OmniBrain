"""Upload validation helpers."""

import logging
from pathlib import Path

from fastapi import UploadFile

from app.config import Settings
from app.utils.exceptions import CorruptedFile, FileTooLarge, InvalidFileType

logger = logging.getLogger(__name__)

PDF_HEADER = b"%PDF-"


def _has_pdf_extension(filename: str) -> bool:
    return Path(filename).suffix.lower() == ".pdf"


async def validate_pdf_upload(file: UploadFile, settings: Settings) -> bytes:
    """Validate an uploaded PDF and return its bytes."""

    filename = file.filename or ""
    content_type = (file.content_type or "").lower()

    if not _has_pdf_extension(filename):
        logger.warning("Rejected unsupported file extension: %s", filename)
        raise InvalidFileType("Only PDF files are supported")

    if content_type not in settings.allowed_mime_types:
        logger.warning("Rejected invalid MIME type for %s: %s", filename, content_type)
        raise InvalidFileType("Invalid MIME type. Only application/pdf is supported")

    content = await file.read()
    await file.seek(0)

    if not content:
        logger.warning("Rejected empty upload: %s", filename)
        raise CorruptedFile("Empty PDF files are not allowed")

    if len(content) > settings.max_upload_size_bytes:
        logger.warning("Rejected oversized upload %s with %d bytes", filename, len(content))
        raise FileTooLarge(f"File exceeds {settings.max_upload_size_mb} MB limit")

    if not content.startswith(PDF_HEADER):
        logger.warning("Rejected corrupted or non-PDF content: %s", filename)
        raise CorruptedFile("Invalid or corrupted PDF file")

    return content

