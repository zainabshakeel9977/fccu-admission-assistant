from typing import List
from config import DocumentChunk
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(documents: List[DocumentChunk], chunk_size: int = 700, chunk_overlap: int = 100):

    """
    Split documents into smaller chunks for embedding and RAG retrieval.

    Args:
        documents: List of DocumentChunk objects
        chunk_size: Max characters per chunk
        chunk_overlap: Overlapping characters between consecutive chunks

    Returns:
        List of chunked DocumentChunk objects with preserved metadata
    """

    chunked_documents = []

    # Initialize the text splitter
    splitter = RecursiveCharacterTextSplitter(chunk_size = chunk_size, chunk_overlap = chunk_overlap)
    
    # Loop through each document
    for document in documents:
        # Split the text into smaller chunks
        splits = splitter.split_text(document.text)

        # Wrap each split in a DocumentChunk and preserve metadata
        for split in splits:
            chunked_documents.append(DocumentChunk(text=split, metadata = document.metadata))
    return chunked_documents

