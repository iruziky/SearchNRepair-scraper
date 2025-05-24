from scrapers.olx_scraper import get_page, next_page, is_last_page
from storage.csv_writer import save_to_csv
from parsers.olx_parser import extract_links 
from parsers.product_parser import *
from datetime import datetime
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
            
            #Tá alterando o link de acesso. não usa mais o do config

            # Não tá identificando a última página
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

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

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

            # Espera que a página carregue minimamente
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            # Verifica se apareceu a mensagem de página não encontrada
            try:
                error_element = driver.find_element(By.CSS_SELECTOR, "div.ad__sc-ka1npw-2:nth-child(2) > span:nth-child(1)")
                if "não foi encontrada" in error_element.text.lower():
                    log("Página não encontrada. Removendo link da lista...")
                    links.pop(0)
                    with open("links.csv", "w") as f:
                        f.writelines(f"{l}\n" for l in links)
                    continue  # Vai pro próximo link
            except NoSuchElementException:
                pass  # Elemento de erro não encontrado, segue normalmente

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
            # driver = init_driver()
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
                "images": get_url_images(driver),
                "isBreak": False
            }

            url = "https://olx-back-end.onrender.com/smartphones/save"
            response = requests.post(url, json=product_data, timeout=10)
            log(f"Status code: {response.status_code}")
            log(f"Response body: {response.text}")

        except Exception as e:
            log(f"Erro ao coletar dados ou enviar para API: {e}")

        links.pop(0)
        with open("links.csv", "w") as f:
            f.writelines(f"{l}\n" for l in links)

        delay = random.uniform(10, 15)
        log(f"Aguardando {delay:.2f} segundos antes de continuar...")
        time.sleep(delay)
