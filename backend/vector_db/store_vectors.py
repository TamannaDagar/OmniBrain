# Import the libraries
from pathlib import Path
import sys
import uuid # for chunk overlap


from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from qdrant_client.models import PointStruct

print("OmniBrain:Vector stores")


# Add vector_db foletr to python path
BASE_DIR= Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

# import file (chunks) to store  in qdrant
from ingestion.chunk_document import chunk_document

# configration
COLLECTION_NAME= 'omnibrain_documents'


# change the file  name whenever you want
#FILENAME= 'sample_document.txt'
# FILENAME= 'sample.pdf'

# for multiple files at a time replace filename

DATA_FOLDER= BASE_DIR/'data'

SUPPORTED_EXTENSIONS= [".txt", ".pdf"]

print("\n OmniBrain: Multiple Document Indexing")


# connect to the Qdrant
print("OmniBrain : Vector Indexing Pipeline")

client= QdrantClient(
    host='localhost',
    port= 6333
)
print("Connected Successfully!")


# find Documents
files= [
    file
    for file in DATA_FOLDER.iterdir()
    if file.suffix.lower() in SUPPORTED_EXTENSIONS]

print(f"Found {len(files)} supported documents")


# Process each doucment
total_documents=0
total_chunks=0
total_vectors=0

# Load the embedding model
model= SentenceTransformer("all-MiniLM-L6-v2")
print(f"Model Loaded: {model}")


for file in files:

    filename = file.name

    print(f"\nProcessing Document: {filename}")

    # Load document
    chunks = chunk_document(filename)

    print(f"Document Loaded: {filename}")

    print("\nGenerating Embeddings...")
    embeddings = model.encode(chunks)

    print(f"Generated {len(embeddings)} embeddings")

    points = []

    for idx, (chunk, embedding) in enumerate(zip(chunks, embeddings), start=1):

        point = PointStruct(
            id=str(uuid.uuid4()),
            vector=embedding.tolist(),
            payload={
                "text": chunk,
                "source_file": filename,
                "chunk_id": idx
            }
        )

        points.append(point)

    print(f"Prepared {len(points)} vectors")

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

    print("Successfully stored vectors!")

    total_documents += 1
    total_chunks += len(chunks)
    total_vectors += len(points)


# Final summary
print("Indexing Completed Successfully")

print(f"Source File: {filename}")
print(f"Documents Indexed : {total_documents}")
print(f"Total Chunks      : {total_chunks}")
print(f"Total Vectors     : {total_vectors}")