# Import the libraries
from pathlib import Path
import sys


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
FILENAME= 'sample.pdf'

# connect to the Qdrant
print("OmniBrain : Vector Indexing Pipeline")

client= QdrantClient(
    host='localhost',
    port= 6333
)
print("Connected Successfully!")


# Load document chunks
chunks= chunk_document(FILENAME)

print(f"Document Loaded: {FILENAME}")


# Load the embedding model
model= SentenceTransformer("all-MiniLM-L6-v2")
print(f"Model Loaded: {model}")

#Sample text
'''texts=[
    "Artificial Intelligence is transforming industries.",
    "Machine Learning helps computers learn from data.",
    "Vector databases enable semantic search.",
    "Python is widely used for AI development.",
    "Qdrant stores embeddings for fast retrieval."
]'''

print("\n Embeddings Generating..")
embeddings= model.encode(chunks)

print(f"Generated {len(embeddings)} embeddings")


# create qdrant points
print("\n Uploading vectors to the Qdrant...")

points=[]


for idx, (chunk, embedding) in enumerate(zip(chunks, embeddings), start=1):

    
        point= PointStruct(
            id= idx,
            vector= embedding.tolist(), # convert generated embedding (numpy array) to the python list for qdrant 
            payload={
                'text': chunk,
                'source_file': FILENAME,
                'chunk_id': idx

            }
        )
        points.append(point)
        print(f"Prepared {len(points)} vectors")


# load in connection
print("\nUploading vectors to Qdrant...")
client.upsert(  # insert or update 
    collection_name=COLLECTION_NAME,
    points=points
)

print(f"\n Successfully stored vectors!")

#Summary
print("Indexing Completed Successfully")


print(f"Collection     : {COLLECTION_NAME}")
print(f"Source File    : {FILENAME}")
print(f"Total Chunks   : {len(chunks)}")
print(f"Total Vectors  : {len(points)}")