# Day 4 Notes

## What is a Point in Qdrant?

A point is a single record stored inside a collection.

Each point contains:

- Unique ID
- Vector
- Payload (metadata)

## Why do we need Payload?

The vector helps Qdrant find similar content.

The payload stores information about the vector, such as the original sentence.

Without payload, we would know which vector is similar but not what text it represents.