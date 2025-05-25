from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageNavigator:
    def __init__(self, driver):
        self.driver = driver

    def get_page(self, url, expected_element):
        self.driver.get(url)
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, expected_element))
            )
        except Exception as e:
            print(f"Error loading the page: {e}")
            raise