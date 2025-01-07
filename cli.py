import argparse
from research_papers_cli import PubMedClient, extract_non_academic_authors
import csv
import requests

# Main function to handle command-line operations
def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(
        description="Fetch research papers from PubMed and process results into a CSV file."
    )
    parser.add_argument("query", type=str, help="Query string for PubMed search.")
    parser.add_argument("-f", "--file", type=str, help="Output CSV file.")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode.")
    # parser.add_argument("-h", "--help", action="help", help="Display usage instructions.")

    # Parse the arguments
    args = parser.parse_args()

    # Initialize PubMed client
    client = PubMedClient()

    try:
        # Search for papers using the query
        ids = client.search_papers(args.query)
        details = client.fetch_paper_details(ids)

        # Print debug information if enabled
        if args.debug:
            print(f"Fetched {len(ids)} papers from PubMed.")

        rows = []
        # Process each paper's details
        for paper_id, paper_details in details.items():
            if paper_id == "uids":  # Skip metadata key
                continue
            non_academic_authors, affiliations = extract_non_academic_authors(paper_details)
            rows.append({
                "PubMedID": paper_id,
                "Title": paper_details.get("title", "Unknown"),
                "Publication Date": paper_details.get("pubdate", "Unknown"),
                "Non-academic Author(s)": ", ".join(non_academic_authors),
                "Company Affiliation(s)": ", ".join(affiliations),
                "Corresponding Author Email": paper_details.get("email", "Unknown"),
            })

        # Write results to a CSV file or print to the console
        if args.file:
            with open(args.file, "w", newline="", encoding="utf-8") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=rows[0].keys())
                writer.writeheader()
                writer.writerows(rows)
        else:
            print(rows)

    except requests.exceptions.RequestException as e:
        print(f"Error while fetching data from PubMed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the CLI program
if __name__ == "__main__":
    main()
