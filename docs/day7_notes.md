# 📅 OmniBrain Project – Day 7 Notes
**Role:** Vector Database Engineer

---

# 🎯 Objective

Improve the RAG indexing pipeline by making it closer to a production-ready system.

Instead of indexing a single document with simple chunking, today's goal was to implement better document processing and scalable indexing.

---

# ✅ Task 1 – Smart Chunking (Concept)

## What I Learned

Initially, my system was using:

- One line = One chunk

This approach works for small text files but is not suitable for large PDFs because important information may be split between chunks.

I learned that production RAG systems use smarter chunking strategies to preserve context and improve retrieval quality.

---

# ✅ Task 2 – Fixed-Size Chunking

## Previous Approach

```python
document.split("\n")
```

Every line became one chunk.

---

## New Approach

Implemented fixed-size chunking.

```python
chunk_size = 300
```

The document is cleaned first:

```python
document = " ".join(document.split())
```

Then divided into equal-sized chunks.

### Benefits

- Consistent chunk size
- Works for TXT and PDF
- Independent of document formatting
- Better for embedding generation

---

# ✅ Task 3 – Chunk Overlap

Implemented overlapping chunks.

Example:

Without overlap

```
Chunk 1
ABCDEFGHIJ

Chunk 2
KLMNOPQRST
```

With overlap

```
Chunk 1
ABCDEFGHIJ

Chunk 2
HIJKLMNOPQ
```

Overlap keeps some text shared between consecutive chunks.

### Benefits

- Preserves context
- Improves semantic retrieval
- Better search accuracy

---

# ✅ Task 4 – UUID for Vector IDs

Previously vectors were stored like:

```
1
2
3
```

This could overwrite existing vectors if new documents were indexed.

Now every vector receives a unique identifier:

```python
id = str(uuid.uuid4())
```

### Benefits

- No ID collisions
- Multiple documents can be indexed safely
- Production-ready approach

---

# ✅ Task 5 – Multiple Document Indexing

Earlier the system indexed only one document.

Example:

```python
FILENAME = "sample_document.txt"
```

Now the pipeline automatically scans the data folder.

```python
SUPPORTED_EXTENSIONS = [".txt", ".pdf"]
```

Supported files are indexed automatically.

### Benefits

- No need to manually change filenames
- Easily scalable
- Supports multiple TXT and PDF documents

---

# ✅ Task 6 – End-to-End Testing

Performed complete pipeline testing.

Pipeline:

```
Documents
      ↓
Load Documents
      ↓
Chunk Documents
      ↓
Generate Embeddings
      ↓
Store in Qdrant
      ↓
Semantic Search
```

Tested with:

- sample_document.txt
- sample.pdf

Verified:

- Multiple document indexing
- UUID generation
- Chunk overlap
- Semantic retrieval

---

# 🛠 Problems Faced

## 1. PDF Path Error

Error:

```
FileNotFoundError
```

Reason:

`load_pdf.py` was still pointing to the old `data/pdfs` directory.

Solution:

Updated the path to:

```python
BASE_DIR.parent / "data" / filename
```

---

## 2. Wrong Indentation

Problem:

Only one document was being indexed.

Reason:

Most of the indexing logic was outside the `for file in files:` loop.

Solution:

Moved the entire indexing pipeline inside the loop.

---

## 3. Payload Issue

Initially stored:

```python
source_file = DATA_FOLDER
```

Corrected to:

```python
source_file = filename
```

Now every chunk stores the correct source document.

---

## 4. Old Collection Data

Old vectors caused duplicate search results.

Solution:

Deleted the Qdrant collection.

Recreated the collection.

Indexed documents again.

---

# 📂 Files Modified

```
chunk_document.py
```

Changes:

- Fixed-size chunking
- Chunk overlap

---

```
store_vectors.py
```

Changes:

- UUID
- Multiple document indexing
- Automatic scanning of data folder

---

```
load_pdf.py
```

Changes:

- Updated PDF path

---

# 📚 Concepts Learned

- Fixed-size chunking
- Chunk overlap
- UUID
- Metadata payload
- Multiple document indexing
- Production RAG ingestion
- End-to-end indexing pipeline

---

# 🎤 Interview Questions I Can Answer

## 1. Why is chunking required?

Chunking divides large documents into smaller pieces so embeddings capture local context. It improves retrieval speed and accuracy.

---

## 2. Why use chunk overlap?

Chunk overlap preserves context between adjacent chunks, preventing important information from being split at chunk boundaries.

---

## 3. Why use UUID instead of sequential IDs?

Sequential IDs can overwrite existing vectors. UUIDs guarantee unique identifiers, allowing safe indexing of multiple documents.

---

## 4. Why store metadata?

Metadata such as:

- source_file
- chunk_id

helps identify where a retrieved chunk originated.

---

## 5. How does your indexing pipeline work?

```
Load Document
      ↓
Clean Text
      ↓
Fixed-size Chunking
      ↓
Chunk Overlap
      ↓
Embedding Generation
      ↓
Create Payload
      ↓
Store in Qdrant
```

---

# 🚀 Git Commits

```
git commit -m "Implement fixed-size document chunking"
```

```
git commit -m "Implement overlapping chunk strategy"
```

```
git commit -m "Use UUIDs for unique vector IDs"
```

```
git commit -m "Support indexing multiple documents from data folder"
```

```
git commit -m "Validate end-to-end document indexing and retrieval pipeline"
```

---

# 📈 Day 7 Outcome

Successfully upgraded the OmniBrain RAG pipeline with:

- ✅ Fixed-size chunking
- ✅ Chunk overlap
- ✅ UUID-based vector IDs
- ✅ Multiple document indexing
- ✅ Updated payload metadata
- ✅ End-to-end indexing and retrieval testing

The project is now significantly closer to a production-ready RAG indexing pipeline.