from scrapers.olx_scraper import get_page, next_page, is_last_page
from parsers.olx_parser import extract_links
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def product_links_scraper(driver):
    """Coleta todos os links de produtos das páginas de listagem"""
    driver = get_page(driver)
    index = 1
    all_links = []

    while True:
        try:
            # Extrai links da página atual
            links = extract_links(driver)
            all_links.extend(links)
            print(f"Página {index} com {len(links)} links")

            # Verifica se é a última página antes de tentar ir para próxima
            if is_last_page(driver):
                print("Última página alcançada.")
                break

            # Vai para próxima página
            index += 1
            next_page(driver, index)

            # Pequena pausa para evitar detecção
            time.sleep(2)

        except Exception as e:
            print(f"Erro durante scraping de links: {e}")
            break

    return all_links

def products_scraper(driver):
    """Raspa os detalhes dos produtos individuais"""
    links = product_links_scraper(driver)
    
    if not links:
        print("Nenhum link encontrado para scraping.")
        return

    for i, link in enumerate(links[:5], 1):  # exemplo: raspa só 5 primeiros
        try:
            print(f"\nProcessando produto {i}/{min(5, len(links))}...")
            
            # Navega para a página do produto
            driver.get(link)
            
            # Espera explícita pelo elemento da descrição
            try:
                desc_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.sc-ifAKCX.kZqjtz"))
                )
                desc = desc_element.text
            except:
                desc = "Descrição não encontrada"
            
            print(f"Link: {link}\nDescrição: {desc}\n{'='*50}")
            
        except Exception as e:
            print(f"Erro ao processar o link {link}: {e}")
            continue