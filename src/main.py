from scrapers.olx_scraper import get_page_content
from parsers.olx_parser import parse_listings
from storage.csv_writer import save_to_csv

def main():
    html = get_page_content()
    listings = parse_listings(html)
    save_to_csv(listings)

if __name__ == "__main__":
    main()
