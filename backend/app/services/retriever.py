from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

# Configuration constants
QDRANT_URL = "http://localhost:6333" # URL of Qdrant server
COLLECTION_NAME = "fccu_admissions"  # Name of collection in Qdrant
EMBED_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"  # Embedding model
TOP_K = 5  # Number of results to retrieve

# Initialize Qdrant client
client = QdrantClient(url = QDRANT_URL)
# Load embedding model
embedder = SentenceTransformer(EMBED_MODEL_NAME)

# Function to retrieve relevant chunks from Qdrant
def retrieve_chunks(query: str, program: str, top_k: int = TOP_K):
    
    # Convert query text into vector embedding
    query_vector = embedder.encode(query).tolist()
    # Perform vector search in Qdrant
    query_results = client.query_points( #Returns Query Response Object
        collection_name = COLLECTION_NAME, 
        query = query_vector, 
        limit = top_k, 
        with_payload = True, 
        query_filter = {      # Filter results by program
            "must":[
                {
                    "key":"program_level", 
                    "match": {"value":program}
                }
            ]
        }
    ) 

    return query_results



def build_context(results):

    # Initialize containers for the combined text and the citation metadata
    context = ""
    sources = []
    
    # Iterate through each search result returned by the vector_database
    for retrieved_chunk in results:
        # Extract the data dictionary (payload) from the result object
        payload = retrieved_chunk.payload
        # Safely extract values, providing defaults if keys are missing
        context += f"\n{payload.get("text","")}\n"
        source_name = payload.get("source_name","unknown")
        page_number = payload.get("page_number","N/A")
        # Add a dictionary of metadata to our sources list for referencing later
        sources.append(({
            "source_name":source_name,
            "page_number":page_number
        }))

    # Return both the flattened text and the list of source references
    return context, sources



