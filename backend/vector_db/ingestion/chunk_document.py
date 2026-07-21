# import the libraries
'''from pathlib import Path

print("\n OmniBrain: Document Chunking..")

#locate the file
BASE_DIR= Path(__file__).resolve().parent
file_path= BASE_DIR.parent /"data" / "sample_document.txt"

# read the document
with open(file_path, "r", encoding="utf-8") as file:
    document= file.read()


# Split document into chunks (one sentence per chunk)
chunks= [line.strip() for line in document.split ("\n") if  line.strip() ]# remove unwanted space- line.strip(), # document.split- splits whenever te new linne appears

print(f"Total Chunks: {len(chunks)}") #one sentence per chunk


for i, chunk in enumerate(chunks, start=1):
    print(f"Chunk: {i}")
    print(chunk)'''




# replacing for pipeline for reading the text file

## importing  the load_document file
from pathlib import Path
import sys

# Add backend/vector_db to Python path
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR.parent))


from ingestion.load_document import load_document

# start chunking
def chunk_document (filename):
    document= load_document(filename)


    chunks= [
        line.strip()
        for line in document.split("\n")
        if line.strip()
    ]
    return chunks  # again no print statement