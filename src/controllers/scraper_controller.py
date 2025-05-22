from scrapers.olx_scraper import get_page, next_page, is_last_page
from parsers.olx_parser import extract_links
from storage.csv_writer import save_to_csv
import time

def product_links_scraper(p):
    index = 1
    browser, page = get_page(p)

    while not is_last_page(page):
        links = extract_links(page)
        save_to_csv(links)
        next_page(page, index)
        index += 1

    browser.close()

def products_scraper(p):
    links = open("links.csv").read()
    links = links.split("\n")

    page = get_page(p)
    for link in links:
        time.sleep(15)
        page.goto(link)

    print(links)