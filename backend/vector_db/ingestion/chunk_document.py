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
'''from pathlib import Path
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
    return chunks  # again no print statement '''



## combine both text + pdf file
# import libraries
import sys
from pathlib import Path

BASE_DIR= Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR.parent))

from ingestion.load_document import load_document
from ingestion.load_pdf import load_pdf

def get_document(filename):

    '''
    Load document based on file extension.
    '''

    if filename.lower().endswith(".txt"):
        return load_document(filename)

    elif filename.lower().endswith(".pdf"):
        return load_pdf(filename)

    else:
        raise ValueError(f"Unsupported File Format: {filename}")




def chunk_document(filename):
    """
    Load the document and split it into chunks.
    Currently, one line = one chunk.
    """
    document= get_document(filename)

    chunks= [
        line.strip()
        for line in document.split("\n")
        if line.strip()
    ]

    return chunks

if __name__== "__main__":
    print("OmniBrain: Document Chunking..")


    # give any file name text or pdf based on your testing
    #filename= ('sample_document.txt')

    #now test with pdf
    filename= ('sample.pdf')

    chunks=chunk_document(filename)

    print(f'Document: {filename}')
    print(f"Total Chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks,start=1):
        print(f'Chunk: {i}')
        print(chunk)




    