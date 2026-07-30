# Day 8 – Retrieval Pipeline Improvements

**Project:** OmniBrain – Intelligent RAG System  
**Role:** Vector Database Engineer  
**Day:** 8

---

# Objective

The objective of Day 8 was to improve the retrieval system of OmniBrain and make it closer to a production-level semantic search application.

Instead of retrieving a single chunk, the system was enhanced to:

- Understand semantic similarity
- Use cosine similarity effectively
- Retrieve Top-K results
- Filter irrelevant results
- Build an interactive search application
- Display professional search output

---

# Topics Covered

## 1. Similarity Search

Previously, we stored embeddings in Qdrant.

Today we learned how Qdrant retrieves relevant chunks.

### Retrieval Process

```text
User Query
      │
      ▼
Generate Query Embedding
      │
      ▼
Compare with Stored Embeddings
      │
      ▼
Cosine Similarity
      │
      ▼
Return Most Similar Chunks
```

### Important Points

- Qdrant never compares plain text.
- It compares embeddings.
- Both document chunks and user queries are converted into vectors using the same embedding model.
- The nearest vectors are returned as search results.

---

# 2. Cosine Similarity

Cosine Similarity is the mathematical function used to compare two vectors.

Instead of comparing words, it compares the direction of vectors.

### Similarity Range

| Score | Meaning |
|--------|----------|
| 1.0 | Perfect Match |
| 0.7 – 0.9 | Strong Match |
| 0.5 – 0.7 | Good Match |
| 0.3 – 0.5 | Moderate Match |
| Below 0.3 | Weak Match |

### Why Cosine Similarity?

Cosine similarity measures semantic similarity instead of exact keyword matching.

This makes retrieval more accurate.

---

# 3. Top-K Retrieval

Initially our system retrieved only one chunk.

```text
Query
   │
   ▼
Best Chunk
```

Production systems retrieve multiple chunks.

```text
Query
   │
   ▼
Top 3 Chunks
```

### Benefits

- Better context
- Better answers
- Higher retrieval accuracy
- Useful for RAG systems

### Code

```python
TOP_K = 3

results = client.query_points(
    collection_name=COLLECTION_NAME,
    query=query_vector,
    limit=TOP_K,
    with_payload=True
).points
```

---

# 4. Similarity Threshold

Top-K retrieval may include irrelevant chunks.

To avoid this, we introduced a similarity threshold.

```python
SIMILARITY_THRESHOLD = 0.40
```

Example

```
0.83 ✅

0.76 ✅

0.18 ❌ Ignore
```

Implementation

```python
for result in results:

    if result.score < SIMILARITY_THRESHOLD:
        continue
```

### Benefits

- Removes weak matches
- Cleaner retrieval
- Better context for LLM

---

# 5. Interactive Semantic Search

Instead of restarting the application every time, we converted it into an interactive search program.

Before

```
Run Program

↓

Ask Query

↓

Program Ends
```

After

```
Run Program

↓

Ask Query

↓

Ask Another Query

↓

Exit
```

Implementation

```python
while True:

    query = input("Enter your query: ").strip()

    if query.lower() == "exit":
        break
```

---

# 6. Input Validation

We handled invalid user input.

Example

```python
if not query:
    print("Please enter a valid query.")
    continue
```

Benefits

- Prevents empty searches
- Better user experience

---

# 7. No Relevant Results Handling

If all retrieved chunks have very low similarity, the application now displays a proper message.

Implementation

```python
found = False

for result in results:

    if result.score < SIMILARITY_THRESHOLD:
        continue

    found = True

if not found:
    print("No relevant results found.")
```

---

# 8. Professional Search Output

The output was redesigned.

Now it displays

- Result Number
- Similarity Score
- Source File
- Chunk ID
- Retrieved Text
- Search Summary
- Retrieval Time

Example

```
==================================================
Result #1
==================================================

Similarity Score : 0.7812

Source File : sample_document.txt

Chunk ID : 1

Text:

Artificial Intelligence is transforming industries.
```

---

# 9. Retrieval Time

We measured the search execution time.

Implementation

```python
import time

start_time = time.time()

...

end_time = time.time()

retrieval_time = end_time - start_time
```

Example

```
Search Time : 0.0824 seconds
```

Benefits

- Performance monitoring
- Useful for optimization
- Production metric

---

# Final Retrieval Pipeline

```
User Query
      │
      ▼
Generate Query Embedding
      │
      ▼
Search Qdrant
      │
      ▼
Cosine Similarity
      │
      ▼
Top-K Results
      │
      ▼
Similarity Threshold
      │
      ▼
Professional Output
```

---

# Complete OmniBrain Pipeline

```
Document
    │
    ▼
TXT / PDF Loader
    │
    ▼
Chunking
    │
    ▼
Generate Embeddings
(all-MiniLM-L6-v2)
    │
    ▼
Store in Qdrant
───────────────────────────────
User Query
    │
    ▼
Generate Query Embedding
    │
    ▼
Qdrant Similarity Search
    │
    ▼
Cosine Similarity
    │
    ▼
Top-K Retrieval
    │
    ▼
Similarity Threshold
    │
    ▼
Display Results
```

---

# Concepts Learned

- Semantic Search
- Similarity Search
- Cosine Similarity
- Query Embeddings
- Top-K Retrieval
- Similarity Threshold
- Interactive CLI
- Retrieval Time
- Search Summary
- Professional Output Formatting

---

# Interview Questions

## Q1. How does Qdrant retrieve relevant chunks?

**Answer**

Qdrant converts both the user's query and document chunks into embeddings using the same embedding model. It compares the query embedding with the stored embeddings using cosine similarity and returns the Top-K most similar chunks.

---

## Q2. What is Cosine Similarity?

**Answer**

Cosine similarity is a mathematical measure used to compare the direction of two vectors. In OmniBrain, it is used to compare query embeddings with document embeddings for semantic retrieval.

---

## Q3. Why use Top-K Retrieval?

**Answer**

A user's answer may span multiple document chunks. Retrieving the Top-K most similar chunks provides richer context to the language model, resulting in more accurate and complete responses.

---

## Q4. Why use a Similarity Threshold?

**Answer**

A similarity threshold filters out weakly related chunks so that only relevant context is passed to the language model, improving answer quality.

---

## Q5. Why did you measure retrieval time?

**Answer**

Retrieval time is an important performance metric. It helps evaluate the efficiency of the vector database and monitor search performance as the dataset grows.

---

# Files Updated

```
backend/
└── vector_db/
    └── search_vectors.py
```

---

# Git Commit

```bash
git add .

git commit -m "Day 8: Enhanced semantic retrieval with Top-K search, similarity threshold, interactive CLI, and retrieval metrics"

git push origin feature/vector-db
```

---

# Day 8 Outcome

✅ Learned semantic similarity retrieval

✅ Understood cosine similarity

✅ Implemented Top-K retrieval

✅ Added similarity threshold

✅ Built interactive semantic search

✅ Added retrieval metrics

✅ Created production-style search output

---

# Progress



**Project Completion:** **80%**

---

# Next Day Preview (Day 9)

- Introduction to Retrieval-Augmented Generation (RAG)
- Understanding Retrieval vs Generation
- Integrating an LLM with the retrieval pipeline
- Prompt engineering for RAG
- End-to-end RAG workflow
- Testing and evaluating generated answers