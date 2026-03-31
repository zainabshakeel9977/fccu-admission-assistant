from ingestion.config import DocumentChunk
import cloudscraper
from bs4 import BeautifulSoup

webpages_name_map = {
    r"https://www.fccollege.edu.pk/bs-programs/":"Bachelor of Studies (BS) Admissions 2026 - FCCU University",
    r"https://www.fccollege.edu.pk/pharmd-admissions/":"PharmD Admissions - FCCU University",
    r"https://www.fccollege.edu.pk/accuplacer-sat-ap/":"ACCUPLACER/SAT/AP (Collegeboard) - FCCU University",
    r"https://www.fccollege.edu.pk/programs-offered/":"Postgraduate Programs 2026 - FCCU University",
    r"https://cppg.fccollege.edu.pk/admissions-timeline/":"Admissions & Timeline – CPPG",
    r"https://www.fccollege.edu.pk/postgraduate-in-business/":"Postgraduate in Business - FCCU University",
    r"https://www.fccollege.edu.pk/postgraduate-in-clinical-psychology/":"Postgraduate in Clinical Psychology - FCCU University",
    r"https://www.fccollege.edu.pk/postgraduate-in-computer-science/":"Postgraduate in Computer Sciences - FCCU University",
    r"https://www.fccollege.edu.pk/postgraduate-in-economics/":"Postgraduate in Economics - FCCU University",
    r"https://www.fccollege.edu.pk/postgraduate-in-biological-sciences/":"Postgraduate in Biological Sciences - FCCU University",
    r"https://www.fccollege.edu.pk/postgraduate-in-chemistry/":"Postgraduate in Chemistry - FCCU University",
    r"https://www.fccollege.edu.pk/postgraduate-in-physics/":"Postgraduate in Physics - FCCU University",
    r"https://www.fccollege.edu.pk/postgraduate-in-biblical-studies/":"Postgraduate in Biblical Studies - FCCU University",
    r"https://www.fccollege.edu.pk/mphil-education/":"MPhil Education - FCCU University",
    r"https://www.fccollege.edu.pk/postgraduate-in-english/":"Postgraduate in English - FCCU University",
    r"https://www.fccollege.edu.pk/postgraduate-in-environmental-sciences/":"Postgraduate in Environmental Sciences - FCCU University",
    r"https://www.fccollege.edu.pk/mphil-mass-communication/":"MPhil Mass Communication - FCCU University",
    r"https://www.fccollege.edu.pk/postgraduate-in-political-science/":"Postgraduate in Political Science - FCCU University",
    r"https://www.fccollege.edu.pk/mphil-sociology/":"MPhil Sociology - FCCU University",
    r"https://www.fccollege.edu.pk/postgraduate-in-statistics/":"Postgraduate in Statistics - FCCU University",
    r"https://www.fccollege.edu.pk/admissions/":"Admissions - FCCU University",
    r"https://www.fccollege.edu.pk/fccu-homepage/financial-aid-scholarships/":"Financial Aid And Scholarships - FCCU University",
    r"https://www.fccollege.edu.pk/residential-life/":"Residential Life - FCCU University",
    r"https://www.fccollege.edu.pk/tuition-fee/":"Tuition Fee - FCCU University",
    r"https://www.fccollege.edu.pk/tuition-fee/fee-payment-through-1-bill-integration/":"Fee Payment Through 1 Bill Integration - FCCU University"
}

def load_webpage(url:str, program: str) -> DocumentChunk:

    scraper = cloudscraper.create_scraper()

    try: 
        response = scraper.get(url, timeout=15)

        if response.status_code == 403:
            print("Status Code 403: Forbidden")
            return None
        
        soup = BeautifulSoup(response.text, "html.parser")
        for element in soup(["script", "nav", "footer","header","style"]):
            element.decompose()

        webpage_text = soup.get_text(separator=" ", strip = True)

        return DocumentChunk(
            text=webpage_text,
            metadata={
                "program_level": program,
                "source_type":"web",
                "source_name":webpages_name_map.get(url),
                "source_path": url,
            }
        )              

    except Exception as e:
        print(f"Error: {e}")
        return None



