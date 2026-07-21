# Day 4 Notes - Storing and Searching Vectors in Qdrant

## Objective

Learn how to store embeddings in a Qdrant collection and perform semantic search using vector similarity.

---

## What is a Point in Qdrant?

A point is a single record stored in a Qdrant collection.

Each point contains:
- Unique ID
- Vector (Embedding)
- Payload (Metadata)

Example:

ID: 1

Vector:
[-0.23, 0.41, ..., 384 values]

Payload:
{
    "text": "Artificial Intelligence is transforming industries."
}

---

## Why is Payload Important?

The vector is used for similarity search.

The payload stores additional information about the vector, such as:
- Original text
- Document name
- Page number
- Metadata

Without the payload, we would know which vector matched but not what information it represents.

---

## What I Implemented

### Task 1
- Understood the structure of a Qdrant Point.
- Learned the importance of payload.

### Task 2
- Connected Python to Qdrant.
- Generated embeddings.
- Stored embeddings in the `omnibrain_documents` collection.

### Task 3
- Verified that vectors were successfully stored.
- Checked collection details and total points.

### Task 4
- Performed semantic search.
- Converted a user query into an embedding.
- Retrieved the most similar vectors using Cosine Similarity.
- Displayed similarity scores and matching text.

### Task 5
- Made the semantic search interactive using `input()`.
- Tested different search queries.

---

## Qdrant Workflow

Text
↓
Sentence Transformer
↓
Embedding (384 Dimensions)
↓
Qdrant Collection
↓
Semantic Search
↓
Top Matching Results

---

## Key Concepts Learned

### Collection
A collection is similar to a table in a relational database. It stores vectors and their payloads.

### Point
A single record inside a collection containing:
- ID
- Vector
- Payload

### Embedding
A numerical representation of text that captures semantic meaning.

### Payload
Metadata associated with a vector.

### Cosine Similarity
Measures how similar two vectors are based on the angle between them.
Higher cosine similarity indicates more similar meanings.

---

## Difference Between SQL Search and Semantic Search

### SQL Search
- Keyword based
- Requires exact word matches

Example:
Search: "Vector Database"

Only rows containing those exact words are returned.

### Semantic Search
- Meaning based
- Uses embeddings
- Finds relevant information even if wording is different

Example:
Query:
"How can I search documents by meaning?"

Result:
"Vector databases enable semantic search."

Although the wording is different, the meaning is similar.

---

## Libraries Used

- sentence-transformers
- qdrant-client
- Docker
- Qdrant

---

## Learning Outcome

Today I learned:
- How vectors are stored in a Vector Database.
- The structure of a Qdrant Point.
- The importance of payload metadata.
- How to verify stored vectors.
- How semantic search works.
- How to retrieve the most relevant information using vector similarity.

---

## Git Commits Completed

- Initialize vector storage module
- Store document embeddings in Qdrant
- Verify stored vectors
- Implement semantic search
- Add interactive semantic search

---

## Next Step (Day 5)

- Store real documents instead of sample text.
- Split large documents into chunks.
- Generate embeddings for each chunk.
- Build the document ingestion pipeline for the RAG system.