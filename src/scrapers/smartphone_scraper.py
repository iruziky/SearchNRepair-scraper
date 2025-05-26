from selenium.webdriver.common.by import By
from utils.helpers import log
from navigation.page_navigation import PageNavigator
from config import SELECTORS

class SmartphoneScraper:
    def __init__(self, driver):
        self.driver = driver
        
    def get_ad_page(self, ad_url) -> bool:
        try:
            navigator = PageNavigator(self.driver)
            navigator.get_page(ad_url, "#description-title > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)")
            
        except Exception as e:
            log(f"Não foi possível carregar {ad_url}, pulando...")
            return False
        
    def is_valid_page(self) -> bool:
        error_elements = self.driver.find_elements(By.CSS_SELECTOR, "div.ad__sc-ka1npw-2:nth-child(2) > span:nth-child(1)")
        if error_elements:
            error_element = error_elements[0]
            if "não foi encontrada" in error_element.text.lower():
                log("Página não encontrada.")
                return False
        return True
    
    def get_url_images(self):
        """Returns list with URLs of carousel images"""
        selector = ".ad__sc-xbkr7e-1"
        response = ""
        carousel_div = self.driver.find_element(By.CSS_SELECTOR, selector)
        images = carousel_div.find_elements(By.TAG_NAME, "img")
        for img in images:
            response += img.get_attribute("src") + ";"
        return response

    def get_elements(self):
        data = {}
        for field, selector in SELECTORS.items():
            try:
                element = self.driver.find_element(By.CSS_SELECTOR, selector)
                data[field] = element.text.strip()
            except Exception:
                data[field] = f"{field} not found"
        data["link"] = self.driver.current_url
        data["images"] = self.get_url_images()
        return data