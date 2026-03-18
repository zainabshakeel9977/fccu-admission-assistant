from ingestion.config import DocumentChunk
import requests
from bs4 import BeautifulSoup

def load_webpage(url: str, program: str) -> DocumentChunk:
    """
    Load a webpage, extract visible text, and return as a DocumentChunk.
    """

    # Send a GET request to the URL to fetch webpage content
    response = requests.get(url)
    #  Parse the HTML content using BeautifulSoup
    # "html.parser" is Python's built-in parser
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract all visible text from the HTML
    # separator=" " ensures words are separated by spaces
    # strip=True removes leading/trailing whitespace
    webpage_text = soup.get_text(separator=" ", strip = True)
    # Create metadata for this webpage chunk
    webpage_metadata = {"program_level":program,
                         "source_type":"web",
                         "source_url":url}
    #Wrap the text and metadata into a DocumentChunk
    return DocumentChunk(text=webpage_text, metadata=webpage_metadata)

