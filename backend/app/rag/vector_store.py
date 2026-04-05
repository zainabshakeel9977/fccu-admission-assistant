# Import Qdrant client used to communicate with the vector database
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

# Name of the vector collection that will store document embeddings
COLLECTION_NAME = "fccu_admissions"


# Function to create and return a Qdrant client connection
def get_qdrant_client():
    
    # Connect to a locally running Qdrant server
    return QdrantClient(url = "http://localhost:6333")


# Function to ensure that the required collection exists in Qdrant
def ensure_collection(client):
    
    # Fetch all collections currently stored in Qdrant
    collections = client.get_collections().collections
    
    # Extract collection names and check if our collection exists
    if COLLECTION_NAME not in [collection.name for collection in collections]:
        # If the collection does not exist, create it
        print("Creating Collection...")
        client.create_collection(collection_name = 
                                 COLLECTION_NAME, vectors_config = VectorParams
                                 # Dimension of the embedding vector
                # Must match the embedding model (384 for all-MiniLM-L6-v2)
                                 (size = 384, distance = Distance.COSINE),# Distance metric used for similarity search
                                 ) 


client = get_qdrant_client()

# Delete old collection (resets everything)
client.delete_collection(collection_name=COLLECTION_NAME)