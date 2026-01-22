from typing import List
from ingestion.config import DocumentChunk
from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_documents(documents: List[DocumentChunk], chunk_size: int = 700, chunk_overlap: int = 100):

    chunked_documents = []
    splitter = RecursiveCharacterTextSplitter(chunk_size = chunk_size, chunk_overlap = chunk_overlap)

    for document in documents:
        splits = splitter.split_text(document.text)
        for split in splits:
            chunked_documents.append(DocumentChunk(text=split, metadata = document.metadata))
    return chunked_documents

