from pathlib import Path
from PIL import Image
from ingestion.config import DocumentChunk
import pytesseract

# Specify Tesseract OCR executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

images_url_map = {
    r"D:\fccu-admission-assistant\data\raw\images\Bachelors Fee Installment Plan.jpeg": r"https://www.fccollege.edu.pk/wp-content/uploads/2026/01/bachelor-2025-26.jpeg",
    r"D:\fccu-admission-assistant\data\raw\images\Bachelors Fee Structure.png": r"https://www.fccollege.edu.pk/wp-content/uploads/2025/11/Bach.png",
    r"D:\fccu-admission-assistant\data\raw\images\PharmD Fee Installment Plan.jpeg": r"https://www.fccollege.edu.pk/wp-content/uploads/2026/01/d-pharmacy.jpeg",
    r"D:\fccu-admission-assistant\data\raw\images\Bachelors PharmD Fee Structure.png": r"https://www.fccollege.edu.pk/wp-content/uploads/2025/11/Pharma.png",
    r"D:\fccu-admission-assistant\data\raw\images\Postgraduate Fee Installment Plan.jpeg": r"https://www.fccollege.edu.pk/wp-content/uploads/2026/01/postgraduate-deadlines.jpeg",
    r"D:\fccu-admission-assistant\data\raw\images\Postgraduate Fee Structure.png": r"https://www.fccollege.edu.pk/wp-content/uploads/2025/11/Post1.png",
    r"D:\fccu-admission-assistant\data\raw\images\Postgraduate PhD Fee Structure.png": r"https://www.fccollege.edu.pk/wp-content/uploads/2025/11/Phd.png",
    r"D:\fccu-admission-assistant\data\raw\images\Hostel Installment Fee Plan Continuning-2026.png": r"https://www.fccollege.edu.pk/wp-content/uploads/2026/01/installment_fee_plan_continuning-2026.png",
    r"D:\fccu-admission-assistant\data\raw\images\Hostel Installment Fee Plan Freshmen-2026.png": r"https://www.fccollege.edu.pk/wp-content/uploads/2026/01/installment_fee_plan_freshment-2026.png",
}

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
            "source_name":image_path.name,
            "source_path":images_url_map.get(str(image_path))
        }

        print(image_metadata["source_path"])
        print(image_path)
        print(image_text)

      
        return [DocumentChunk(text=image_text, metadata=image_metadata)]

