# Import the libraries

from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from qdrant_client.models import PointStruct

print("OmniBrain:Vector stores")

# connect to the Qdrant
client= QdrantClient(
    host='localhost',
    port= 6333
)


# Load the embedding model
model= SentenceTransformer("all-MiniLM-L6-v2")

#Sample text
texts=[
    "Artificial Intelligence is transforming industries.",
    "Machine Learning helps computers learn from data.",
    "Vector databases enable semantic search.",
    "Python is widely used for AI development.",
    "Qdrant stores embeddings for fast retrieval."
]

print("\n Embeddings Generating..")
embeddings= model.encode(texts)


print("\n Uploading vectors to the Qdrant...")

points=[]


for idx, (text, embedding) in enumerate(zip(texts, embeddings)):

    points.append(
        PointStruct(
            id= idx+1,
            vector= embedding.tolist(),
            payload={
                'text': text
            }
        )
    )


# load in connection
client.upsert(
    collection_name='omnibrain_documents',
    points=points
)

print(f"\n Successfully stored {len(points)} vectors!")