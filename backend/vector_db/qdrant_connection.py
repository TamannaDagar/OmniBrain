# import libraries

from qdrant_client import QdrantClient
print("OmniBrain: Odrant connection Test")

try:
    # connect to te local qdrant server
    client= QdrantClient(
        host= "localhost",
        port= 6333
        )
    
    print("\nSuccessfully connected to the Qdrant")

    #get existing collections
    collections= client.get_collections()

    print("\n Current collections:")
    print(collections)

except Exception as e :
    print("\n Connection failed!")
    print(e)