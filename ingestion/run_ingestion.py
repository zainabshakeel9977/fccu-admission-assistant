
import sys
from pathlib import Path

# Make project root discoverable
root_directory = Path(__file__).parent.parent.resolve() # one level up from ingestion folder
sys.path.insert(0, str(root_directory))
#__file__ gives absolute path of current file
#resolve converts into absolute path
#sys.path is list of directories where python searches for modules. It expects directories paths in string format. sys.path[0] is searched first


from ingestion.loaders.pdf_loader import load_pdf
from ingestion.loaders.web_loader import load_webpage
from ingestion.loaders.image_loader import load_image
from ingestion.chunking.chunker import chunk_documents

from backend.app.rag.embeddings import EmbeddingModel
from backend.app.rag.vector_store  import (get_qdrant_client, COLLECTION_NAME, ensure_collection)


def main():
    """
    Main ingestion pipeline for the FCCU Admission Assistant.

    Steps:
    1. Load documents from PDFs, images, and web pages.
    2. Chunk large texts into smaller pieces for embeddings.
    3. Generate embeddings for each text chunk.
    4. Insert embeddings and metadata into the Qdrant vector database.
    """

    #Initialize a list to hold all documents from different sources
    documents_list = []
    
    # ---------- Load PDFs ----------
    pdf_directory = Path(r"D:\fccu-admission-assistant\data\raw\pdfs")
    for pdf in pdf_directory.glob("*.pdf"): # Iterate over all PDF files

        pdf_title = pdf.name
        
        # Determine program level from filename
        if "bachelors" in pdf_title.lower():
            program = "bachelors"
        elif "postgraduate" in pdf_title.lower():
            program = "postgraduate"
        else: 
            program = "both"
        # Load PDF and extend the main documents list with DocumentChunk objects
        documents_list.extend(load_pdf(pdf,program))
    

    # ---------- Load Images ----------
    image_directory = Path(r"D:\fccu-admission-assistant\data\raw\images")

    for img in image_directory.glob("*"): # Iterate over all image files

        img_title = img.name
        # Determine program level from filename
        if "bachelors" in img_title.lower() or "pharmd" in img_title.lower():
            program = "bachelors"
        else:
            program = "postgraduate"
        
        # Load image using OCR and append to the documents list
        documents_list.extend(load_image(img,program))

    # ---------- Load Web Pages ----------
    with open(r"D:\fccu-admission-assistant\data\raw\urls.txt", "r") as file:
        program_level = "bachelors" # Default program level
        for line in file:
            line = line.strip()
            if not line:
                continue
            # Lines starting with '#' define program level for next URLs
            elif line.startswith("#"):
                if line.startswith("#Postgraduate"):
                    program_level = "postgraduate"
                if line.startswith("#Both"):
                    program_level = "both"
            else:
                # Load webpage text and append as DocumentChunk
                documents_list.append(load_webpage(line, program_level))

    #Chunk all documents into smaller pieces for embeddings
    chunks = chunk_documents(documents_list)
    
    # Create embeddings for all chunks
    embedder = EmbeddingModel()
    chunks_text = [chunk.text  for chunk in chunks] # Extract plain text
    embeddings = embedder.embed(chunks_text)

    print(f"Embeddings count: {len(embeddings)}")
    
    
    #Connect to Qdrant vector database and ensure the collection exists
    client = get_qdrant_client()
    ensure_collection(client)
    
    #Upsert (insert or update) all chunks into Qdrant
    # Each chunk becomes a point with:
    # - 'id': unique index
    # - 'vector': embedding
    # - 'payload': metadata + original text
    client.upsert(
       collection_name=COLLECTION_NAME, 
       points = [
           {
               "id":idx, 
               "vector":embeddings[idx],
               "payload": chunks[idx].metadata | {"text": chunks[idx].text},
           }
           for idx in range(len(chunks))
       ]
    )

    print(f"Ingestion Completed Successfully")


if __name__ =="__main__":
    main()


