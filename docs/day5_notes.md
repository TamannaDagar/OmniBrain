# Day 5 Notes - Document Ingestion Pipeline

## Objective

Build the first stage of a production-ready RAG (Retrieval-Augmented Generation) pipeline by replacing hardcoded text with real documents.

---

# Why Document Ingestion?

Previously, embeddings were generated from hardcoded Python lists.

Example:

```python
texts = [
    "Artificial Intelligence is transforming industries.",
    "Machine Learning helps computers learn from data."
]
```

This approach is not scalable.

Instead, production AI systems read documents from files such as:

- TXT
- PDF
- DOCX
- HTML

These documents are processed before generating embeddings.

---

# Document Ingestion Pipeline

Document
↓
Load Document
↓
Chunk Document
↓
Generate Embeddings
↓
Store in Qdrant
↓
Semantic Search

---

# Task 1 - Project Structure

Created folders for document ingestion.

```
backend/
└── vector_db/
    ├── data/
    ├── ingestion/
    ├── embeddings/
```

Purpose:

- **data/** stores source documents.
- **ingestion/** contains document processing code.
- **embeddings/** contains embedding-related modules.

---

# Task 2 - Document Loader

Created:

```
load_document.py
```

Purpose:

- Reads a text document.
- Returns the document content.
- Uses `pathlib` for portable file handling.

Key Concepts:

- `Path(__file__)`
- `BASE_DIR`
- Relative paths

---

# Why Use BASE_DIR?

Instead of:

```python
Path("../data/sample_document.txt")
```

we used:

```python
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR.parent / "data" / "sample_document.txt"
```

Advantages:

- Works on every computer.
- Independent of terminal location.
- Easier for team collaboration.
- Production-ready approach.

---

# Task 3 - Document Chunking

Created:

```
chunk_document.py
```

Purpose:

Split a large document into smaller chunks.

Current Strategy:

One sentence = One chunk

Example:

Document

```
AI is transforming industries.
Machine Learning learns from data.
Vector databases store embeddings.
```

↓

Chunks

```
Chunk 1
AI is transforming industries.

Chunk 2
Machine Learning learns from data.

Chunk 3
Vector databases store embeddings.
```

---

# Why Chunk Documents?

Large documents produce poor embeddings.

Smaller chunks:

- Improve retrieval accuracy.
- Reduce unnecessary context.
- Increase search performance.
- Help Large Language Models generate better responses.

---

# Task 4 - Modular Programming

Instead of one large script:

```
Read File
↓

Chunk
↓

Print
```

we created reusable functions.

```
load_document()

↓

Returns Document

↓

chunk_document()

↓

Returns Chunks

↓

Another module uses them
```

Benefits:

- Reusable
- Easy to test
- Easier maintenance
- Cleaner code

---

# Python Concepts Learned

## pathlib

Used for platform-independent file paths.

Example:

```python
BASE_DIR = Path(__file__).resolve().parent
```

---

## Functions

Instead of printing inside every script:

```python
return document
```

This allows other modules to reuse the data.

---

## Modular Programming

Each file has one responsibility.

Example:

```
load_document.py
```

Reads documents only.

```
chunk_document.py
```

Splits documents only.

This follows the **Single Responsibility Principle (SRP)**.

---

# Current Project Workflow

TXT Document
↓
Load Document
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

- pathlib
- sentence-transformers
- qdrant-client
- Docker
- Qdrant

---

# Learning Outcome

Today I learned:

- How production AI systems load documents.
- Why document ingestion is important.
- How to build reusable Python modules.
- How to use `pathlib` for robust file handling.
- Why document chunking improves semantic search.
- How modular programming makes projects scalable.

---

# Git Commits Completed

- Set up document ingestion structure
- Implement document loader
- Implement document chunking
- Refactor ingestion into modular pipeline

---

# Next Step (Day 6)

- Read PDF documents.
- Extract text from PDFs.
- Clean extracted text.
- Implement smart chunking.
- Store PDF chunks in Qdrant.
- Search information from PDF documents.