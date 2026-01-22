from pathlib import Path
from PIL import Image
from ingestion.config import DocumentChunk
import pytesseract

def load_image(image_path: Path, program: str)-> List[DocumentChunk]:

    image = Image.open(image_path)
    image_text = pytesseract.image_to_string(image)
    image_text = image_text.strip()
    
    if not image_text:
        return []
    else:
        image_metadata = {
            "program level": program,
            "source type":image, 
            "source name":image_path.name
        }
        return [DocumentChunk(text=image_text, metadata=image_metadata)]