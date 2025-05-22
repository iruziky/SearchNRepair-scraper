from scrapers.olx_scraper import get_page, next_page, is_last_page
from parsers.olx_parser import extract_links 
from storage.csv_writer import save_to_csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def product_links_scraper(driver):
    """Collect all product links from listing pages"""
    driver = get_page(driver)
    index = 1

    while True:
        try:
            links = extract_links(driver)
            save_to_csv(links)
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
    links = open("links.csv").read()
    links = links.split("\n")
    
    if not links:
        print("No links found for scraping.")
        return

    for i, link in enumerate(links[:5], 1):
        try:
            print(f"\nProcessing product {i}/{min(5, len(links))}...")
            
            driver.get(link)
            
            try:
                desc_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.sc-ifAKCX.kZqjtz"))
                )
                desc = desc_element.text
            except:
                desc = "Description not found"
            
            print(f"Link: {link}\nDescription: {desc}\n{'='*50}")
            
        except Exception as e:
            print(f"Error processing link {link}: {e}")
            continue