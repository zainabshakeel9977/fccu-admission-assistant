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


def main():
    
    # Take user query input
    query = input("Enter your admission query")
    # Take program input and normalize it
    program = input("Enter your program (bachelors/postgraduate)").strip().lower()
    # Retrieve relevant chunks
    query_results = retrieve_chunks(query, program)
    print(query_results)
    print(len(query_results.points))
    # Loop through results and display them
    for i, chunk in enumerate(query_results.points): #Query Response object has attribute points, which is a list of scored points. Each scored point is a class with the following attributes: id, score, payload, vector
        payload = chunk.payload
        print(f"--------Chunk {i+1}--------")
        print(f"Score: {chunk.score}")
        print(f"Source: {payload.get("source_name")}")
        print(f"Page: {payload.get("page_number")}")
        print(f"Text: {payload.get("text")[:500]}")
        print()


if __name__ == "__main__":
    main()