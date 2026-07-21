# import libraries
'''from pathlib import Path

print("\n OmniBrain: Document Loader...")

# file location
file_path= Path("D:/OmniBrain/OmniBrain/backend/vector_db/data/sample_document.txt")

# reading the document
try:
    with open(file_path, "r", encoding='utf-8') as file:  #eads the file safely
        document= file.read()      # read the entire document

        print("\n Document Loaded successfully!") # load document converts into python string then chunks

except FileNotFoundError:
    print(f"\n Document with file_path {file_path} not fond")'''


## for pipeline main connection with emedding models 
# another file use it no print statement
from pathlib import Path

print("\n Document loading..")

BASE_DIR= Path(__file__).resolve().parent


def load_document (filename):
    file_path= BASE_DIR.parent /"data"/ filename

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()