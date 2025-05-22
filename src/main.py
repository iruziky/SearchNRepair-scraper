from playwright.sync_api import sync_playwright
from controllers.scraper_controller import product_links_scraper

def main():
    with sync_playwright() as p:
        product_links_scraper(p)

if __name__ == "__main__":
    main()
