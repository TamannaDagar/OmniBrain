# Day 6 Notes - PDF Processing and Document Indexing

## Objective

Extend the document ingestion pipeline to support PDF documents and integrate both TXT and PDF files into a common vector indexing workflow.

---

# What Was Built Today?

The document ingestion pipeline was enhanced to support multiple document formats.

Supported file types:

- TXT
- PDF

Both file types now follow the same indexing pipeline.

---

# Updated RAG Pipeline

Document (TXT / PDF)
        │
        ▼
Document Loader
        │
        ▼
Extract Text
        │
        ▼
Chunk Document
        │
        ▼
Generate Embeddings
        │
        ▼
Store in Qdrant
        │
        ▼
Semantic Search

---

# Task 1 - Install PyMuPDF

Installed:

```
pymupdf
```

Imported as:

```python
import fitz
```

Purpose:

- Read PDF files.
- Extract text page by page.
- Build reusable PDF ingestion modules.

---

# Why PyMuPDF?

Advantages:

- Fast
- Accurate
- Lightweight
- Widely used in AI applications
- Supports large PDF documents

---

# Task 2 - PDF Loader

Created:

```
load_pdf.py
```

Responsibilities:

- Open PDF document.
- Read every page.
- Extract text.
- Return the complete document as a string.

Example Workflow:

PDF

↓

Page 1

↓

Page 2

↓

Page 3

↓

Combined Text

---

# Task 3 - Common Ingestion Pipeline

Instead of separate pipelines:

TXT

↓

TXT Loader

PDF

↓

PDF Loader

A common loader function was introduced.

```
Document
        │
        ▼
Load TXT or PDF
        │
        ▼
Return Text
```

This makes the project scalable and easier to maintain.

---

# Why Modular Programming?

Every module has one responsibility.

Example:

load_document.py

↓

Loads TXT files

load_pdf.py

↓

Loads PDF files

chunk_document.py

↓

Splits text into chunks

store_vectors.py

↓

Stores embeddings into Qdrant

search_vectors.py

↓

Performs semantic search

Advantages:

- Easy to maintain
- Easy to test
- Easy to extend
- Reusable components

---

# Task 4 - Dynamic Vector Indexing

Previously:

```python
texts = [
    "...",
    "...",
]
```

Now:

```python
chunks = chunk_document(filename)
```

The system automatically:

- Loads document
- Chunks document
- Generates embeddings
- Stores vectors

No hardcoded text is required.

---

# Metadata in Payload

Each vector now stores additional information.

Example:

```python
payload = {
    "text": chunk,
    "source_file": filename,
    "chunk_id": idx
}
```

---

# Why Metadata?

Without metadata:

```
Vector

↓

Matched
```

No information about the source document.

With metadata:

```
Matched Vector

↓

Source File

↓

Chunk Number

↓

Original Text
```

This is essential in production RAG systems.

---

# Qdrant Payload Example

```
Vector
│
├── Embedding
│
└── Payload
        │
        ├── text
        ├── source_file
        └── chunk_id
```

---

# Semantic Search Improvement

Search results now include:

- Similarity Score
- Source File
- Chunk ID
- Original Text

Example:

```
Result 1

Similarity Score : 0.9234

Source File : sample.pdf

Chunk ID : 5

Text

Vector databases enable semantic search.
```

---

# Python Concepts Learned

## pathlib

Used to create platform-independent file paths.

Example:

```python
BASE_DIR = Path(__file__).resolve().parent
```

Benefits:

- Portable
- Cross-platform
- Reliable

---

## sys.path

Used to import modules from project folders.

Example:

```python
sys.path.append(str(BASE_DIR))
```

---

## Functions

Reusable functions:

- load_document()
- load_pdf()
- chunk_document()

Each function performs one task.

---

# Software Engineering Concepts

## Single Responsibility Principle (SRP)

Each module performs only one responsibility.

Examples:

load_pdf.py

↓

Read PDF

chunk_document.py

↓

Split text

store_vectors.py

↓

Store vectors

---

## Open/Closed Principle

The pipeline can support new document types without changing the chunking logic.

Example:

Today:

- TXT
- PDF

Tomorrow:

- DOCX
- HTML
- Markdown

Only a new loader is needed.

---

# Current Project Architecture

```
backend/
└── vector_db/
    ├── data/
    │      ├── sample_document.txt
    │      └── pdfs/
    │             └── sample.pdf
    │
    ├── ingestion/
    │      ├── load_document.py
    │      ├── load_pdf.py
    │      └── chunk_document.py
    │
    ├── store_vectors.py
    ├── search_vectors.py
    ├── verify_vectors.py
    └── create_collection.py
```

---

# Current Workflow

TXT / PDF

↓

Load Document

↓

Extract Text

↓

Chunk Document

↓

Generate Embeddings

↓

Store in Qdrant

↓

Semantic Search

---

# Libraries Used

- PyMuPDF (fitz)
- sentence-transformers
- qdrant-client
- Docker
- Qdrant
- pathlib

---

# Challenges Faced

## 1. Import Errors

Problem:

```
ModuleNotFoundError
```

Solution:

Used:

```python
sys.path.append(...)
```

to correctly import project modules.

---

## 2. Missing Payload Keys

Problem:

```
KeyError: source_file
```

Cause:

Older vectors were indexed before metadata was added.

Solution:

- Recreate the collection.
- Re-index all documents.
- Use `.get()` when reading payload values.

Example:

```python
result.payload.get("source_file", "Unknown")
```

---

# Learning Outcome

Today I learned:

- How PDF text extraction works.
- How to build a reusable PDF loader.
- How to support multiple document types using one pipeline.
- How metadata improves semantic search.
- How to build a scalable indexing workflow.
- Why modular programming is important in AI applications.
- How production RAG systems prepare documents before indexing.

---

# Git Commits Completed

- Add PyMuPDF dependency
- Implement PDF loader
- Integrate PDF loader into chunking pipeline
- Update vector indexing for dynamic documents
- Enhance semantic search with metadata

---

# Progress Summary

Completed:

✅ Environment Setup

✅ Sentence Embeddings

✅ Docker + Qdrant

✅ Collection Creation

✅ Vector Storage

✅ Semantic Search

✅ TXT Loader

✅ PDF Loader

✅ Document Chunking

✅ Dynamic Document Indexing

Current Completion:

Approximately **60%** of the Vector Database Engineer module is complete.

---

# Next Step (Day 7)

Upcoming improvements:

- Smart chunking
- Chunk overlap
- UUID-based vector IDs
- Multiple document indexing
- Batch processing
- Improved semantic search
- Production-ready indexing pipeline