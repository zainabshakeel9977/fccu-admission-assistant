from ingestion.config import DocumentChunk
import requests
from bs4 import BeautifulSoup

def load_webpage(url: str, program: str) -> DocumentChunk:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    webpage_text = soup.get_text(separator=" ", strip = True)
    webpage_metadata = {"program level":program,
                         "source type":"web",
                         "source url":url}
    return DocumentChunk(text=webpage_text, metadata=webpage_metadata)

