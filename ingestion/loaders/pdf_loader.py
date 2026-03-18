from ingestion.config import DocumentChunk
from pathlib import Path
from typing import List
import fitz




def load_pdf(pdf_path: Path, program: str) -> List[DocumentChunk]:
    
    """
    Load a PDF, extract text per page, and return a list of DocumentChunk objects.
    """

    pdf_chunks = []
    pdf_doc = fitz.open(pdf_path)
    # Loop through PDF pages
    for page_number, page_content in enumerate(pdf_doc, start = 1):
        page_text = page_content.get_text().strip()
        
        if page_text: 
            page_metadata = {
                "program_level":program, 
                "source_type":"PDF", 
                "source_name":pdf_path.name,
                "page_number":page_number
            }
            pdf_chunks.append(DocumentChunk(text=page_text,metadata=page_metadata))
    
    return pdf_chunks


