from ingestion.config import DocumentChunk
from pathlib import Path
from typing import List
import fitz

pdfs_url_map = {
    r"D:\fccu-admission-assistant\data\raw\pdfs\Bachelors-Admissions-List-of-majors-.pdf": r"https://www.fccollege.edu.pk/wp-content/uploads/2025/09/List-of-majors-Bachelor-Admissions.pdf",
    r"D:\fccu-admission-assistant\data\raw\pdfs\Bachelors-Catalog-2025-26-updated.pdf": r"https://www.fccollege.edu.pk/wp-content/uploads/2025/12/Bachelors-Catalog-2025-26-updated.pdf",
    r"D:\fccu-admission-assistant\data\raw\pdfs\Bachelors-Transfer Credit Policy.pdf": r"https://drive.google.com/file/d/1BRbrYwntPR0n2mPvKtshS6wRv6U-zf3Y/view",
    r"D:\fccu-admission-assistant\data\raw\pdfs\Hostel-Policy-61119.pdf": r"https://www.fccollege.edu.pk/wp-content/uploads/Hostel-Policy-61119.pdf",
    r"D:\fccu-admission-assistant\data\raw\pdfs\Payment-procedure-FC-IB-MCB-Live.pdf": r"https://www.fccollege.edu.pk/wp-content/uploads/Payment-procedure-FC-IB-MCB-Live.pdf",
    r"D:\fccu-admission-assistant\data\raw\pdfs\Postgraduate-Catalog-25-26-dec.pdf": r"https://www.fccollege.edu.pk/wp-content/uploads/2025/12/PG-Catalog-25-26-dec.pdf"
}

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
                "source_path":pdfs_url_map.get(str(pdf_path)),
                "page_number":page_number
            }
            pdf_chunks.append(DocumentChunk(text=page_text,metadata=page_metadata))

    
    return pdf_chunks


