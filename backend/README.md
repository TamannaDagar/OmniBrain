# OmniBrain Backend

Production-ready FastAPI backend for accepting PDF uploads, validating them,
storing them securely, scheduling placeholder ingestion, and exposing document
processing status.

## Features

- Async `POST /upload` endpoint for PDF uploads
- PDF extension, MIME type, size, empty-file, and header validation
- Secure UUID-prefixed file storage under `app/uploads`
- FastAPI `BackgroundTasks` ingestion placeholder
- Replaceable in-memory document status store
- `GET /status/{document_id}` and `GET /health`
- Centralized exception handling with standardized JSON errors
- File and console logging under `app/logs/backend.log`
- Swagger and ReDoc documentation

## Requirements

- Python 3.12+

## Setup

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

## Backend Structure

backend/
├── app/
│   ├── api/
│   ├── services/
│   ├── models/
│   ├── utils/
│   ├── uploads/
│   ├── logs/
│   ├── config.py
│   └── main.py
├── requirements.txt
├── .env.example
└── README.md

## Processing Workflow

Client
   │
   ▼
POST /upload
   │
   ▼
Validate PDF
   │
   ▼
Store File
   │
   ▼
Generate Document ID
   │
   ▼
Trigger Background Ingestion
   │
   ▼
Return Processing Status
   │
   ▼
GET /status/{document_id}

## Run

```bash
uvicorn app.main:app --reload
```

Open:

- Swagger: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- Health: http://127.0.0.1:8000/health

## API

### POST /upload

Multipart form upload field:

- `file`: PDF file, maximum 100 MB by default

Successful response:

```json
{
  "success": true,
  "document_id": "6a1fbb78-fc3b-45d4-a55f-122b06d39e10",
  "filename": "4cbf82_report.pdf",
  "status": "Processing",
  "message": "Upload successful"
}
```

### GET /status/{document_id}

Successful response:

```json
{
  "document_id": "6a1fbb78-fc3b-45d4-a55f-122b06d39e10",
  "status": "Completed",
  "message": "Document processing completed"
}
```

### GET /health

Successful response:

```json
{
  "success": true,
  "status": "ok",
  "message": "OmniBrain backend is running"
}
```

## Error Format

```json
{
  "success": false,
  "error": "Invalid PDF file"
}
```

Validation errors include field-level details.

## Future Integration Points

The current ingestion service intentionally uses `simulate_processing(document_id)`
as a placeholder. PDF parsing, chunking, embedding generation, and Qdrant writes
can be added behind the service layer without changing the public REST contract.

