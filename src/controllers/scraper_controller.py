from scrapers.olx_scraper import get_page, next_page, is_last_page
from storage.csv_writer import save_to_csv
from parsers.olx_parser import extract_links 
from parsers.product_parser import (
    get_title,
    get_price,
    get_category,
    get_brand,
    get_model,
    get_condition,
    get_memory,
    get_color,
    get_battery_life,
    get_description,
    get_url_images,
)

import time
import random
import requests

def search_page_scraper(driver):
    """Collect all product links from listing pages"""
    driver = get_page(driver)
    index = 1

    while True:
        try:
            links = extract_links(driver)

            rows = [[link] for link in links]
            save_to_csv(rows, "links.csv")

            print(f"Page {index} with {len(links)} links")

            if is_last_page(driver):
                print("Last page reached.")
                break

            index += 1
            next_page(driver, index)

            time.sleep(2)

        except Exception as e:
            print(f"Error during links scraping: {e}")
            break

def products_scraper(driver):
    """Scrape details of individual products"""
    with open("links.csv") as f:
        links = [line.strip() for line in f if line.strip()]
    
    if not links:
        print("No links found for scraping.")
        return
    
    products_data = []
    for i, link in enumerate(links, 1):
        print(f"\nScraping product {i}/{len(links)}: {link}")
        driver.get(link)
        
        product_data = {
            "link": link,
            "title": get_title(driver),
            "price": get_price(driver),
            "category": get_category(driver),
            "brand": get_brand(driver),
            "model": get_model(driver),
            "condition": get_condition(driver),
            "memory": get_memory(driver),
            "color": get_color(driver),
            "batteryLife": get_battery_life(driver),
            "description": get_description(driver),
            "images": get_url_images(driver)
        }

        url = "http://localhost:8080/smartphones/save"

        response = requests.post(url, json=product_data)

        print("Status code:", response.status_code)
        print("Response body:", response.text)

        time.sleep(random.uniform(3, 6))