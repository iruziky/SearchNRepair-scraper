from scrapers.olx_scraper import get_page, next_page, is_last_page
from parsers.olx_parser import extract_links
from storage.csv_writer import save_to_csv

def product_links_scraper(p):
    index = 1
    browser, page = get_page(p)

    while not is_last_page(page):
        links = extract_links(page)
        save_to_csv(links)
        next_page(page, index)
        index += 1

    browser.close()
