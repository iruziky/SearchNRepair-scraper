from playwright.sync_api import sync_playwright
from scrapers.olx_scraper import get_page
from parsers.olx_parser import extract_links

def main():
    with sync_playwright() as p:
        browser, page = get_page(p)
        links = extract_links(page)

        for link in links:
            print(link)
            
        browser.close()

if __name__ == "__main__":
    main()