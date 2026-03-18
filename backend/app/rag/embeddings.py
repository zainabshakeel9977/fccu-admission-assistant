from sentence_transformers import SentenceTransformer

# A wrapper class for handling text embeddings
class EmbeddingModel():

    def __init__(self):
        # Load a pretrained embedding model
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    
    # text: expects a list of strings
    # returns: a list of embedding vectors (list of float lists)
    def embed(self, text: list[str])-> list[list[float]]:

        # Convert text into vector embeddings
        # Convert NumPy array to a Python list (needed for vector databases)
        return self.model.encode(text, convert_to_numpy=True).tolist()

 