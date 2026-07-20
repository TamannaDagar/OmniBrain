"""Status and health API router."""

from fastapi import APIRouter, Path, status

from app.models.response_models import (
    ErrorResponse,
    HealthResponse,
    StatusResponse,
    ValidationErrorResponse,
)
from app.services.ingestion_service import status_store

router = APIRouter(tags=["Status"])


@router.get(
    "/status/{document_id}",
    summary="Get document processing status",
    description="Returns the current processing state for an uploaded document.",
    response_model=StatusResponse,
    status_code=status.HTTP_200_OK,
    responses={
        404: {"model": ErrorResponse, "description": "Document id does not exist"},
        422: {"model": ValidationErrorResponse, "description": "Request validation error"},
        500: {"model": ErrorResponse, "description": "Internal server error"},
    },
)
async def get_document_status(
    document_id: str = Path(..., min_length=1, description="Document id returned by /upload"),
) -> StatusResponse:
    """Return processing status for a document."""

    status_record = status_store.get_status(document_id)
    return StatusResponse(
        document_id=document_id,
        status=status_record.status,
        message=status_record.message,
    )


@router.get(
    "/health",
    summary="Health check",
    description="Confirms the OmniBrain backend is running.",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    responses={500: {"model": ErrorResponse, "description": "Internal server error"}},
)
async def health_check() -> HealthResponse:
    """Return backend health status."""

    return HealthResponse()

