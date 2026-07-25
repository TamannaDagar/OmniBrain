from qdrant_client import QdrantClient

COLLECTION_NAME= 'omnibrain_documents'

client= QdrantClient(
    host='localhost',
    port=6333
)

try:
    client.delete_collection(collection_name=COLLECTION_NAME)
    print(f"Collection named {COLLECTION_NAME} deleted successfully !")

except Exception as e:
    print(f"error: {e}")