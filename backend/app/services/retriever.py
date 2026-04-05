from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer, CrossEncoder

# Configuration constants
QDRANT_URL = "http://localhost:6333" # URL of Qdrant server
COLLECTION_NAME = "fccu_admissions"  # Name of collection in Qdrant
EMBED_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"  # Embedding model
RERANK_MODEL_NAME = "cross-encoder/ms-macro-MiniLM-L-6-v2" 

INITIAL_RETRIEVE_K = 7 #Number of results to retrieve
TOP_K = 5  # Number of reranked results



# Initialize Qdrant client
client = QdrantClient(url = QDRANT_URL)
# Load embedding model
embedder = SentenceTransformer(EMBED_MODEL_NAME)
reranker = CrossEncoder(RERANK_MODEL_NAME)








# Function to retrieve relevant chunks from Qdrant
def retrieve_chunks(query: str, program: str, top_k: int = INITIAL_RETRIEVE_K):
    
    # Convert query text into vector embedding
    query_vector = embedder.encode(query).tolist()
    # Perform vector search in Qdrant
    query_results = client.query_points( #Returns Query Response Object
        collection_name = COLLECTION_NAME, 
        query = query_vector, 
        limit = top_k, 
        with_payload = True, 
        query_filter = {      # Filter results by program
            
                "should":[
                {
                    "key":"program_level", 
                    "match": {"value":program}
                },
                {
                    "key":"program_level", 
                    "match": {"value":"both"}
                },
                ]
        
        }
    ) 

    return query_results.points


def rerank_chunks(query: str, points: list):
    
    # Prepare (query, chunk_text) pairs
    pairs = [(query, point.payload.get("text","")) for point in points]
    # Get relevance scores
    scores = reranker.predict(pairs)
    # Attach scores
    for i, point in enumerate(points):
        point.payload["rerank_score"] = float(scores[i])
    # Sort by rerank score (descending)
    points.sort(key = lambda a: a.payload["rerank_score"], reverse= True)
    # Return top 5
    return points[:TOP_K]
    


def filter_by_score(results, threshold = 0.4):
      # Return only those results whose score meets or exceeds the threshold
      return [r for r in results if r.payload.get("rerank_score",0) >=threshold]


def build_context(results):

    # Initialize containers for the combined text and the citation metadata
    context = ""
    source_map = {}
    
    # Iterate through each search result returned by the vector_database
    for retrieved_chunk in results:
        # Extract the data dictionary (payload) from the result object
        payload = retrieved_chunk.payload
        # Safely extract values, providing defaults if keys are missing
        context += f"\n{payload.get('text','')}\n"
        source_name = payload.get("source_name","unknown")
        page_number = payload.get("page_number","N/A")
        source_path = payload.get("source_path","unknown")

        if source_path not in source_map:
            if payload.get("source_type").lower()=="pdf":
              source_map[source_path] = {
              "page_number":{page_number},
              "source_name":source_name,
              "source_path":source_path
            }
              
            else:
                source_map[source_path] = {
                 "source_name":source_name,
                 "source_path":source_path
                }

        if source_path in source_map and payload.get("source_type").lower()=="pdf":
            source_map[source_path]["page_number"].add(page_number)
        

    sources = []

    for source_path, data in source_map.items():

        if data.get("page_number"):
           pages = sorted(list(data["page_number"]))
           for page in pages:
                sources.append({
                    "page_number":page,
                    "source_name":data["source_name"],
                    "source_path":data["source_path"]
                })
        
        else:
            sources.append({      
                    "source_name":data["source_name"],
                    "source_path":data["source_path"]
            })
            


    # Return both the flattened text and the list of source references
    return context, sources

