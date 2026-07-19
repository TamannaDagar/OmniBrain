# OmniBrain

FastAPI backend for uploading PDF documents and starting an ingestion workflow.

## Features

- Async PDF upload API
- PDF file validation
- Local document storage
- Background ingestion trigger
- Processing status endpoint
- API exception handling
- Swagger docs through FastAPI

## Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```