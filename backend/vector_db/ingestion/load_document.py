# import libraries
from pathlib import Path

print("\n OmniBrain: Document Loader...")

# file location
file_path= Path("D:/OmniBrain/OmniBrain/backend/vector_db/data/sample_document.txt")

# reading the document
try:
    with open(file_path, "r", encoding='utf-8') as file:  #eads the file safely
        document= file.read()      # read the entire document

        print("\n Document Loaded successfully!")

except FileNotFoundError:
    print(f"\n Document with file_path {file_path} not fond")