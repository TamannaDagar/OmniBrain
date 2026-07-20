"""Response models exposed by the OmniBrain API."""

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class ProcessingStatus(StrEnum):
    """Supported document processing states."""

    QUEUED = "Queued"
    PROCESSING = "Processing"
    COMPLETED = "Completed"
    FAILED = "Failed"


class UploadResponse(BaseModel):
    """Response returned after a PDF upload is accepted."""

    success: bool = Field(default=True, examples=[True])
    document_id: str = Field(examples=["6a1fbb78-fc3b-45d4-a55f-122b06d39e10"])
    filename: str = Field(examples=["4cbf82_report.pdf"])
    status: ProcessingStatus = Field(examples=[ProcessingStatus.PROCESSING])
    message: str = Field(examples=["Upload successful"])

    model_config = ConfigDict(use_enum_values=True)


class StatusResponse(BaseModel):
    """Response returned for document processing status lookups."""

    document_id: str = Field(examples=["6a1fbb78-fc3b-45d4-a55f-122b06d39e10"])
    status: ProcessingStatus = Field(examples=[ProcessingStatus.PROCESSING])
    message: str = Field(examples=["Document is being processed"])

    model_config = ConfigDict(use_enum_values=True)


class HealthResponse(BaseModel):
    """Health check response."""

    success: bool = Field(default=True, examples=[True])
    status: str = Field(default="ok", examples=["ok"])
    message: str = Field(default="OmniBrain backend is running")


class ErrorResponse(BaseModel):
    """Standard error response."""

    success: bool = Field(default=False, examples=[False])
    error: str = Field(examples=["Invalid PDF file"])


class ValidationErrorDetail(BaseModel):
    """Simplified validation error detail."""

    field: str = Field(examples=["file"])
    message: str = Field(examples=["Field required"])


class ValidationErrorResponse(BaseModel):
    """Standard request validation error response."""

    success: bool = Field(default=False, examples=[False])
    error: str = Field(default="Validation error")
    details: list[ValidationErrorDetail] = Field(default_factory=list)

