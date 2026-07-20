# import libarries
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

print("OmniBrain: Create Collection")

# set up the connection
client= QdrantClient(
    host="localhost",
    port= 6333
)

# give collection name
collection_name= "omnibrain_documents"


# condition if the collection- omnibrain_documents already exist
existing=[
    collection.name
    for collection in client.get_collections().collections
]

if collection_name in existing:
    print(f"\n Collection '{collection_name}' already exist!")


# if not exist then create new collection 
else:
    client.create_collection(
        collection_name= collection_name,
        vectors_config= VectorParams(
            size= 384,
            distance=Distance.COSINE
        )
    )
print(f"\n collection '{collection_name}' created successfully!")
