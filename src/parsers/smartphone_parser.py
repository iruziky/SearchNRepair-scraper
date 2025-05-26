from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import SELECTORS
from models.smartphone import Smartphone

def build_smartphone(data):
    smartphone = Smartphone(
        link=data["link"],
        title=data["title"],
        price=data["price"],
        category=data["category"],
        brand=data["brand"],
        model=data["model"],
        condition=data["condition"],
        memory=data["memory"],
        color=data["color"],
        batteryLife=data["batteryLife"],
        description=data["description"],
        images=data["images"],
        isBreak=False
    )
    
    return smartphone