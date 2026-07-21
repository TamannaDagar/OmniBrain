# import from chunk_document
from pathlib import Path
import sys

# Add backend/vector_db to Python path
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR.parent))



from ingestion.chunk_document import chunk_document

print("\n Testing Document Pipeline..")


# document name
chunks= chunk_document('sample_document.txt')

print(f"\n Total Chunks: {len(chunks)} ")


for i, chunk in enumerate(chunks, start=1):
    print(f"\n Chunk: {i}")
    print(chunk)