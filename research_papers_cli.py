import requests
import csv
from typing import List, Dict, Tuple, Optional

# Class to interact with the PubMed API
class PubMedClient:
    BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"  # API for searching papers
    DETAILS_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"  # API for fetching paper details
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the PubMedClient with an optional API key.
        """
        self.api_key = api_key

    def search_papers(self, query: str) -> List[str]:
        """
        Search for papers using PubMed API and return a list of PubMed IDs.
        :param query: Query string for PubMed search.
        :return: List of PubMed IDs.
        """
        params = {
            "db": "pubmed",
            "term": query,
            "retmode": "json",
            "apikey": self.api_key,
        }
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()  # Raise an error for HTTP issues
        return response.json().get("esearchresult", {}).get("idlist", [])

    def fetch_paper_details(self, ids: List[str]) -> List[Dict]:
        """
        Fetch details of papers using PubMed IDs.
        :param ids: List of PubMed IDs.
        :return: List of paper details as dictionaries.
        """
        params = {
            "db": "pubmed",
            "id": ",".join(ids),
            "retmode": "json",
            "apikey": self.api_key,
        }
        response = requests.get(self.DETAILS_URL, params=params)
        response.raise_for_status()  # Raise an error for HTTP issues
        return response.json().get("result", {})


# Function to identify non-academic authors and their affiliations
def extract_non_academic_authors(details: Dict) -> Tuple[List[str], List[str]]:
    """
    Extract non-academic authors and their affiliations based on heuristics.
    :param details: Dictionary containing paper details.
    :return: Tuple of non-academic authors and their affiliations.
    """
    non_academic_authors = []
    affiliations = []
    for author in details.get("authors", []):
        if "university" not in author.get("affiliation", "").lower():  # Check if the author is non-academic
            non_academic_authors.append(author["name"])
            affiliations.append(author.get("affiliation", "Unknown"))
    return non_academic_authors, affiliations
