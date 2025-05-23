from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_url_images(driver):
    """Returns list with URLs of carousel images"""
    try:
        carousel_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ad__sc-xbkr7e-1"))
        )
        images = carousel_div.find_elements(By.TAG_NAME, "img")
        return [img.get_attribute("src") for img in images]
    except Exception:
        return []

def get_description(driver):
    try:
        desc_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ad__sc-2mjlki-1"))
        )
        description = desc_element.text
        return description
    except:
        description = "Description not found"

def get_price(driver):
    """Returns price text"""
    try:
        price = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".olx-text--title-large"))
        ).text
        return price
    except:
        return "Price not found"

def get_title(driver):
    """Returns title text"""
    try:
        title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#description-title > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)"))
        ).text
        return title
    except:
        return "Title not found"

def get_category(driver):
    """Returns category text"""
    try:
        category = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ad__sc-2h9gkk-3"))
        ).text
        return category
    except:
        return "Category not found"

def get_brand(driver):
    """Returns brand text"""
    try:
        brand = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.ad__sc-2h9gkk-0:nth-child(2) > div:nth-child(2) > span:nth-child(2)"))
        ).text
        return brand
    except:
        return "Brand not found"

def get_model(driver):
    """Returns model text"""
    try:
        model = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.ad__sc-2h9gkk-0:nth-child(3) > div:nth-child(2) > span:nth-child(2)"))
        ).text
        return model
    except:
        return "Model not found"

def get_condition(driver):
    """Returns condition text"""
    try:
        condition = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.ad__sc-2h9gkk-0:nth-child(4) > div:nth-child(2) > span:nth-child(2)"))
        ).text
        return condition
    except:
        return "Condition not found"

def get_memory(driver):
    """Returns memory text"""
    try:
        memory = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.ad__sc-2h9gkk-0:nth-child(5) > div:nth-child(2) > span:nth-child(2)"))
        ).text
        return memory
    except:
        return "Memory not found"

def get_color(driver):
    """Returns color text"""
    try:
        color = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.ad__sc-2h9gkk-0:nth-child(6) > div:nth-child(2) > span:nth-child(2)"))
        ).text
        return color
    except:
        return "Color not found"

def get_battery_life(driver):
    """Returns battery life text"""
    try:
        battery_life = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.ad__sc-2h9gkk-0:nth-child(7) > div:nth-child(2) > span:nth-child(2)"))
        ).text
        return battery_life
    except:
        return "Battery life not found"