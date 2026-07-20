"""Custom exceptions and centralized exception handlers."""

import logging

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.models.response_models import ErrorResponse, ValidationErrorResponse

logger = logging.getLogger(__name__)


class OmniBrainError(Exception):
    """Base application exception."""

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = "Internal server error"

    def __init__(self, message: str | None = None) -> None:
        self.message = message or self.message
        super().__init__(self.message)


class InvalidFileType(OmniBrainError):
    """Raised when the uploaded file is not a supported PDF."""

    status_code = status.HTTP_400_BAD_REQUEST
    message = "Invalid PDF file"


class FileTooLarge(OmniBrainError):
    """Raised when an upload exceeds the configured size limit."""

    status_code = status.HTTP_413_CONTENT_TOO_LARGE
    message = "File exceeds the maximum allowed size"


class CorruptedFile(OmniBrainError):
    """Raised when a PDF is empty or cannot pass basic validation."""

    status_code = status.HTTP_400_BAD_REQUEST
    message = "Corrupted or empty PDF file"


class DocumentNotFound(OmniBrainError):
    """Raised when a document id is unknown."""

    status_code = status.HTTP_404_NOT_FOUND
    message = "Document not found"


class InternalServerError(OmniBrainError):
    """Raised for unexpected application failures."""

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = "Internal server error"


def _error_response(status_code: int, message: str) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content=ErrorResponse(error=message).model_dump(),
    )


async def omnibrain_exception_handler(
    request: Request,
    exc: OmniBrainError,
) -> JSONResponse:
    """Return standardized JSON for application exceptions."""

    logger.warning(
        "Application error on %s %s: %s",
        request.method,
        request.url.path,
        exc.message,
    )
    return _error_response(exc.status_code, exc.message)


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
) -> JSONResponse:
    """Return descriptive request validation errors."""

    details = [
        {
            "field": ".".join(str(part) for part in error.get("loc", [])),
            "message": error.get("msg", "Invalid value"),
        }
        for error in exc.errors()
    ]
    logger.warning("Validation error on %s %s: %s", request.method, request.url.path, details)
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=ValidationErrorResponse(details=details).model_dump(),
    )


async def http_exception_handler(
    request: Request,
    exc: StarletteHTTPException,
) -> JSONResponse:
    """Return standardized JSON for framework HTTP exceptions."""

    logger.warning("HTTP error on %s %s: %s", request.method, request.url.path, exc.detail)
    return _error_response(exc.status_code, str(exc.detail))


async def unhandled_exception_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:
    """Log and hide unexpected exception details from clients."""

    logger.exception("Unhandled error on %s %s", request.method, request.url.path)
    return _error_response(status.HTTP_500_INTERNAL_SERVER_ERROR, "Internal server error")


def register_exception_handlers(app: FastAPI) -> None:
    """Attach centralized exception handlers to the FastAPI app."""

    app.add_exception_handler(OmniBrainError, omnibrain_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(Exception, unhandled_exception_handler)
