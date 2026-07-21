# import the libraries
from qdrant_client import QdrantClient

print("\n Verifying the Qdrant")

# setup the connection
client= QdrantClient(
    host="localhost", port= 6333
)

# get the collection name and total points in the collection
collection_info= client.get_collection('omnibrain_documents')

print("\n Collection Name: omnibrain_documents")
print(f"Total Points    : {collection_info.points_count}")

print("\n collection detail")
print(collection_info)