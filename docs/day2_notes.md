# Day 2 Notes - Embedding Generation

## Objective
Learn how to convert text into numerical vectors (embeddings) that can be used for semantic search in a Vector Database.

---

## What is an Embedding?

An embedding is a numerical representation of text. It converts words or sentences into vectors so that a computer can understand their meaning.

Example:

Text:
Artificial Intelligence is transforming industries.

↓

Vector:
[-0.234, 0.451, ..., 384 values]

---

## Why do we use Embeddings?

Computers cannot understand text directly. Embeddings allow computers to compare the meaning of different sentences instead of just matching keywords.

---
## Arcitecture
## Embedding Generation Module

Text
      │
      ▼
Sentence Transformer
      │
      ▼
384-Dimensional Vector
      │
      ▼
NumPy Array
      │
      ▼
Saved as embeddings.npy

---

## Sentence Transformer

We used the model:

all-MiniLM-L6-v2

This model converts each sentence into a **384-dimensional vector** while preserving its semantic meaning.
all- ttrained on all 1-billion text
MiniLM- smaller version of LLM
L6- 6 layers of  transformers(brain of the model)
v2- 2nd latest version 

---

## Output

Input Sentences: 5

Embedding Shape:
(5, 384)

Meaning:
- 5 = Number of input sentences
- 384 = Dimensions of each embedding vector

---

## What I Implemented

- Installed Sentence Transformers.
- Loaded the pre-trained embedding model.
- Generated embeddings for sample sentences.
- Verified the embedding shape.
- Saved embeddings locally for future use.

---

## Learning Outcome

Today I learned:

- What embeddings are.
- Why embeddings are important in RAG systems.
- How Sentence Transformers generate embeddings.
- How to convert text into vectors using Python.
- How embeddings will later be stored in Qdrant for semantic search.

---

## Next Step

- Install and configure Qdrant.
- Store generated embeddings in the Vector Database.
- Perform similarity search using embeddings.