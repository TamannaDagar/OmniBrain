import time

from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient

# ==========================================
# Configuration
# ==========================================

COLLECTION_NAME = "omnibrain_documents"
TOP_K = 3
SIMILARITY_THRESHOLD = 0.40

# ==========================================
# Load Embedding Model
# ==========================================

print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Embedding model loaded successfully!")

# ==========================================
# Connect to Qdrant
# ==========================================

client = QdrantClient(
    host="localhost",
    port=6333
)

print("Connected to Qdrant Successfully!")


print("             OmniBrain Semantic Search")


# ==========================================
# Interactive Search
# ==========================================

while True:

    print("\n" + "-" * 70)

    query = input("Enter your query (type 'exit' to quit): ").strip()

    # Exit Condition
    if query.lower() == "exit":
        print("\nThank you for using OmniBrain!")
        break

    # Empty Query
    if not query:
        print("Please enter a valid query.")
        continue

    # ==========================================
    # Generate Query Embedding
    # ==========================================

    start_time = time.time()

    query_vector = model.encode(query).tolist()

    # ==========================================
    # Search Qdrant
    # ==========================================

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=TOP_K,
        with_payload=True
    ).points

    end_time = time.time()

    retrieval_time = end_time - start_time

    print("\nTop Results\n")

    found = False
    result_number = 1
    relevant_results = 0

    for result in results:

        if result.score < SIMILARITY_THRESHOLD:
            continue

        found = True
        relevant_results += 1

        print("=" * 70)
        print(f"Result #{result_number}")
        print("=" * 70)

        print(f"Similarity Score : {result.score:.4f}")
        print(f"Source File      : {result.payload.get('source_file')}")
        print(f"Chunk ID         : {result.payload.get('chunk_id')}")

        print("\nText:")
        print(result.payload.get("text"))

        result_number += 1

    if not found:
        print("No relevant results found.")

    print("\n" + "=" * 70)
    print("Search Summary")
    print("=" * 70)
    print(f"Relevant Results : {relevant_results}")
    print(f"Search Time      : {retrieval_time:.4f} seconds")
    print("=" * 70)