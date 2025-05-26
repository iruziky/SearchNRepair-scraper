from navigation.page_navigation import PageNavigator
from scrapers.smartphone_scraper import SmartphoneScraper
from scrapers.links_scraper import extract_links 
from parsers.smartphone_parser import build_smartphone
from utils.helpers import log, wait
from api.smartphones import save_smartphone
from api.links import save_links, list_all
from parsers.links_parser import validate_links
import time
import random
from config import BASE_URL, EXPECTED_ELEMENT_SEARCH_PAGE


def search_page_scraper(driver):
    """Collect all product links from listing pages"""
    navigator = PageNavigator(driver)
    page = 1

    while True:
        try:
            navigator.get_page(BASE_URL + str(page), EXPECTED_ELEMENT_SEARCH_PAGE)

            links = extract_links(driver)
            if not links:
                break

            valid_links = validate_links(links)
            if valid_links:
                save_links(valid_links)
                print(f"Page {page} with {len(valid_links)} valid links")

            if not valid_links or len(valid_links) < 50:
                break

            time.sleep(15)
            page += 1

        except Exception as e:
            print(f"Error during links scraping: {e}")


def smartphone_page_scraper(driver):
    """Scrape details of individual products"""

    scraping_links = list_all()
    if not scraping_links:
        log("Nenhum link para scrapear.")
        return

    for contador, scraping_link in enumerate(scraping_links, start=1):
        url = scraping_link["url"]

        log(f"Scraping product {contador}/{len(scraping_links)}: {url}")

        smartphone_scraper = SmartphoneScraper(driver)
        smartphone_scraper.get_ad_page(url)
        smartphone_scraper.is_valid_page()
        data = smartphone_scraper.get_elements()

        smartphone = build_smartphone(data)

        save_smartphone(smartphone)

        if contador % 15 == 0:
            wait(600)
            log("Tempo de espera concluído!")
        else:
            wait(random.uniform(10, 15))
