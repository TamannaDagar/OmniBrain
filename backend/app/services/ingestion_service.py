"""Placeholder ingestion workflow and status store."""

import asyncio
import logging
from dataclasses import dataclass

from app.config import get_settings
from app.models.response_models import ProcessingStatus
from app.utils.exceptions import DocumentNotFound

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class DocumentStatus:
    """Internal status record for an uploaded document."""

    status: ProcessingStatus
    message: str


class InMemoryStatusStore:
    """Replaceable in-memory document status repository."""

    def __init__(self) -> None:
        self._statuses: dict[str, DocumentStatus] = {}

    def set_status(self, document_id: str, status: ProcessingStatus, message: str) -> None:
        """Create or update a document status."""

        self._statuses[document_id] = DocumentStatus(status=status, message=message)
        logger.info("Status changed for %s: %s - %s", document_id, status, message)

    def get_status(self, document_id: str) -> DocumentStatus:
        """Return a document status or raise when it does not exist."""

        status_record = self._statuses.get(document_id)
        if status_record is None:
            logger.warning("Status lookup failed for unknown document_id=%s", document_id)
            raise DocumentNotFound("Document id does not exist")
        return status_record


status_store = InMemoryStatusStore()


async def simulate_processing(document_id: str) -> None:
    """Placeholder for future PDF parsing, chunking, embedding, and vector storage."""

    settings = get_settings()
    try:
        status_store.set_status(
            document_id,
            ProcessingStatus.PROCESSING,
            "Document is being processed",
        )
        await asyncio.sleep(settings.ingestion_delay_seconds)
        status_store.set_status(
            document_id,
            ProcessingStatus.COMPLETED,
            "Document processing completed",
        )
    except Exception:
        logger.exception("Ingestion failed for document_id=%s", document_id)
        status_store.set_status(
            document_id,
            ProcessingStatus.FAILED,
            "Document processing failed",
        )


def queue_document(document_id: str) -> None:
    """Mark a document as queued before background processing starts."""

    status_store.set_status(document_id, ProcessingStatus.QUEUED, "Document queued for processing")

