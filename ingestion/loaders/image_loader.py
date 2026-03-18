from pathlib import Path
from PIL import Image
from ingestion.config import DocumentChunk
import pytesseract

# Specify Tesseract OCR executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def load_image(image_path: Path, program: str)-> list[DocumentChunk]:

    """
    Load an image, extract text using OCR, and return as DocumentChunk.
    """
    # Open the image file
    image = Image.open(image_path)
    # Extract text using OCR
    image_text = pytesseract.image_to_string(image)
    image_text = image_text.strip()

    # Return empty list if no text
    if not image_text:
        return []
    # Create metadata
    else:
        image_metadata = {
            "program_level": program,
            "source_type":"image", 
            "source_name":image_path.name
        }
        return [DocumentChunk(text=image_text, metadata=image_metadata)]

