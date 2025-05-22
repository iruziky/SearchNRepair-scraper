from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL
import time

def get_page(driver):
    """Navigate to the initial page and wait for it to load"""
    driver.get(BASE_URL)
    
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".olx-link.olx-link--caption.olx-link--main"))
        )
    except Exception as e:
        print(f"Error loading the page: {e}")
        raise
    
    return driver

def next_page(driver, index):
    """Navigate to the next results page"""
    driver.get(f"{BASE_URL}?o={index}")
    time.sleep(2)

def is_last_page(driver):
    """Check if it is the last results page"""
    try:
        return "No listings found" in driver.page_source
    except:
        return False