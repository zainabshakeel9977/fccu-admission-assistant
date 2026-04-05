# from huggingface_hub import snapshot_download

# # Pre-download and cache the model
# model_repo = "Qdrant/bm25"

# print(f"Downloading and caching model: {model_repo} ...")
# local_path = snapshot_download(repo_id=model_repo)
# print(f"Model cached at: {local_path}")

from fastembed import SparseTextEmbedding

print("Loading...")
model = SparseTextEmbedding()
print("Done")