from pathlib import Path
from ingestion.loaders.pdf_loader import load_pdf
from ingestion.loaders.web_loader import load_webpage
from ingestion.chunking.chunker import chunk_documents

def main():

    pdf_path = Path("path")
    pdf_chunks = load_pdf(pdf_path, "bachelors")
    chunks = chunk_documents
    print(f"Created {len(chunks)} chunks")


if __name__ =="__main__":
    main()