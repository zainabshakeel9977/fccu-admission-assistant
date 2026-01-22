from ingestion.config import DocumentChunk
from pathlib import Path
from typing import List
import fitz




def load_pdf(pdf_path: Path, program: str) -> List[DocumentChunk]:
    
    pdf_chunks = []
    pdf_doc = fitz.open(pdf_path)
    for page_number, page_content in enumerate(pdf_doc, start = 1):
        page_text = page_content.get_text().strip()
        
        if page_text: 
            page_metadata = {
                "program level":program, 
                "source type":"PDF", 
                "source name":pdf_path.name,
                "page number":page_number
            }
            pdf_chunks.append(DocumentChunk(text=page_text,metadata=page_metadata))
    
    return pdf_chunks


