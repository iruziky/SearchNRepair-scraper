from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL, USER_AGENT, HEADLESS
import time

def get_page(driver):
    """Navega para a página inicial e espera carregar"""
    driver.get(BASE_URL)
    
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".olx-link.olx-link--caption.olx-link--main"))
        )
    except Exception as e:
        print(f"Erro ao carregar a página: {e}")
        raise
    
    return driver

def next_page(driver, index):
    """Navega para a próxima página de resultados"""
    driver.get(f"{BASE_URL}?o={index}")
    time.sleep(2)

def is_last_page(driver):
    """Verifica se é a última página de resultados"""
    try:
        return "Nenhum anúncio foi encontrado" in driver.page_source
    except:
        return False