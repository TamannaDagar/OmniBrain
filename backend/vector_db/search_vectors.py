from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

print("\n OmniBrain Search ..")

# connection setup
client= QdrantClient(
    host="localhost", port=6333
)

# start the model
model= SentenceTransformer("all-MiniLM-L6-v2")

# search query
#query= "How can I perform Semantic Search?"

# allow user too search Query
query= input("\n Enter your query:")

print(f"Search Query: {query}")

# convert into embeddings
query_vector= model.encode(query).tolist()

#Search Qdrant
results= client.query_points(   # start comapring with every vector using cosine
    collection_name= 'omnibrain_documents',
    query= query_vector,
    limit =3
).points

print("\n Top Results \n")

for i, result in enumerate(results, start=1):
    print(f"Result: {i}")
    print(f'Score : {result.score:.4f}')
    print(f'text: {result.payload['text']}')

