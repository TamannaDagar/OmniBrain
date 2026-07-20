"""Upload API router."""

from fastapi import APIRouter, BackgroundTasks, Depends, File, UploadFile, status

from app.config import Settings, get_settings
from app.models.response_models import ErrorResponse, UploadResponse, ValidationErrorResponse
from app.services.file_service import save_pdf_upload
from app.services.ingestion_service import simulate_processing

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post(
    "",
    summary="Upload a PDF document",
    description=(
        "Accepts a PDF file, validates it, stores it securely, and schedules "
        "a background ingestion placeholder. The response is returned immediately."
    ),
    response_model=UploadResponse,
    status_code=status.HTTP_202_ACCEPTED,
    responses={
        400: {"model": ErrorResponse, "description": "Invalid or corrupted PDF file"},
        413: {"model": ErrorResponse, "description": "File exceeds maximum upload size"},
        422: {"model": ValidationErrorResponse, "description": "Request validation error"},
        500: {"model": ErrorResponse, "description": "Internal server error"},
    },
)
async def upload_pdf(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(..., description="PDF file to upload"),
    settings: Settings = Depends(get_settings),
) -> UploadResponse:
    """Upload a PDF and schedule asynchronous document ingestion."""

    response = await save_pdf_upload(file, settings)
    background_tasks.add_task(simulate_processing, response.document_id)
    return response

