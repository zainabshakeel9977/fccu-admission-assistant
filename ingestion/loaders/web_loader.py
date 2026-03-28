import cloudscraper
from bs4 import BeautifulSoup

def load_webpage_robust(url: str, program: str):
    # Create a scraper instance
    scraper = cloudscraper.create_scraper() 
    
    try:
        # Use scraper instead of requests
        response = scraper.get(url, timeout=15)
        
        if response.status_code == 403:
            print("Still blocked by 403. The server is very strict.")
            return None

        soup = BeautifulSoup(response.text, "html.parser")
        
        # Clean up navigation and footer 'garbage'
        for element in soup(["script", "style", "nav", "footer", "header"]):
            element.decompose()

        webpage_text = soup.get_text(separator=" ", strip=True)
        print(f"Success! Extracted {len(webpage_text)} chars.")
        print(webpage_text)
        return webpage_text

    except Exception as e:
        print(f"Error: {e}")
        return None

load_webpage_robust("https://www.fccollege.edu.pk/postgraduate-in-chemistry/", "bachelors")