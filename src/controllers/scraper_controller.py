from scrapers.olx_scraper import get_page, next_page, is_last_page
from storage.csv_writer import save_to_csv
from parsers.olx_parser import extract_links 
from selenium.common.exceptions import WebDriverException
from parsers.product_parser import *
import time
import random
import requests

def search_page_scraper(driver):
    """Collect all product links from listing pages"""
    driver = get_page(driver)
    index = 100

    while True:
        try:
            links = extract_links(driver)

            rows = [[link] for link in links]
            save_to_csv(rows, "links.csv")

            print(f"Page {index} with {len(links)} links")

            # Não tá identificando a última página
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

    for i, link in enumerate(links, 1):
        print(f"\nScraping product {i}/{len(links)}: {link}")
        
        try:
            driver.get(link)
        except WebDriverException as e:
            print(f"Failed to load page {link}: {e}")
            delay = random.uniform(25, 35)
            print(f"Aguardando {delay:.2f} segundos antes de continuar...")
            time.sleep(delay)
            continue

        try:
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

            url = "https://olx-back-end.onrender.com/smartphones/save"
            response = requests.post(url, json=product_data, timeout=10)
            print("Status code:", response.status_code)
            print("Response body:", response.text)

        except Exception as e:
            print("Erro ao coletar dados ou enviar para API:", e)

        delay = random.uniform(25, 35)
        print(f"Aguardando {delay:.2f} segundos antes de continuar...")
        time.sleep(delay)