from playwright.sync_api import sync_playwright
from scrapers.olx_scraper import get_page, next_page, is_last_page
from parsers.olx_parser import extract_links
from storage.csv_writer import save_to_csv

def main():
    with sync_playwright() as p:
        index = 1
        browser, page = get_page(p)

        while(not is_last_page(page)):
            links = extract_links(page)
            save_to_csv(links)
            page, index = next_page(page, index)

        browser.close()

if __name__ == "__main__":
    main()