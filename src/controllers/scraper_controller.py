from scrapers.olx_scraper import get_page, next_page, is_last_page
from parsers.olx_parser import extract_links 
from parsers.product_parser import *
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
from models.smartphone import Smartphone
from utils.helpers import log
from storage.api_client import save_smartphone


def search_page_scraper(driver):
    """Collect all product links from listing pages"""
    driver = get_page(driver)
    index = 1

    while True:
        try:
            links = extract_links(driver)

            rows = [[link] for link in links]
            #save_to_csv(rows, "links.csv")

            print(f"Page {index} with {len(links)} links")
            
            if is_last_page(driver):
                print("Last page reached.")
                break

            index += 1
            next_page(driver, index)

            time.sleep(2)
            break

        except Exception as e:
            print(f"Error during links scraping: {e}")
            break



def products_scraper(driver):
    """Scrape details of individual products"""
    contador = 0

    while True:
        with open("links.csv") as f:
            links = [line.strip() for line in f if line.strip()]
        
        if not links:
            log("No links found for scraping.")
            break

        link = links[0]
        contador += 1

        if contador == 15:
            delay = 600
            log("Aguardando 10 minutos para evitar bloqueio...")
            time.sleep(delay)
            log("Tempo de espera concluído!")
            contador = 0

        log(f"Scraping product {1}/{len(links)}: {link}")

        try:
            driver.set_page_load_timeout(60)
            driver.get(link)

            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            try:
                error_element = driver.find_element(By.CSS_SELECTOR, "div.ad__sc-ka1npw-2:nth-child(2) > span:nth-child(1)")
                if "não foi encontrada" in error_element.text.lower():
                    log("Página não encontrada. Removendo link da lista...")
                    links.pop(0)
                    with open("links.csv", "w") as f:
                        f.writelines(f"{l}\n" for l in links)
                    continue
            except NoSuchElementException:
                pass

        except TimeoutException:
            log(f"Timeout ao carregar {link}, pulando...")
            links.pop(0)
            with open("links.csv", "w") as f:
                f.writelines(f"{l}\n" for l in links)
            continue

        except WebDriverException as e:
            log(f"WebDriverException em {link}: {e}")
            try:
                driver.quit()
            except:
                pass
            continue

        smartphone = Smartphone(
            link=link,
            title=get_title(driver),
            price=get_price(driver),
            category=get_category(driver),
            brand=get_brand(driver),
            model=get_model(driver),
            condition=get_condition(driver),
            memory=get_memory(driver),
            color=get_color(driver),
            batteryLife=get_battery_life(driver),
            description=get_description(driver),
            images=get_url_images(driver),
            isBreak=False
        )
            
        save_smartphone(smartphone)

        links.pop(0)
        with open("links.csv", "w") as f:
            f.writelines(f"{l}\n" for l in links)

        delay = random.uniform(10, 15)
        log(f"Aguardando {delay:.2f} segundos antes de continuar...")
        time.sleep(delay)
