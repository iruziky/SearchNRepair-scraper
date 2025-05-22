from selenium.webdriver.common.by import By

def extract_links(driver):
    tag_links = driver.find_elements(By.CSS_SELECTOR, 'a.olx-adcard__link')
    links = [link.get_attribute('href') for link in tag_links if link.get_attribute('href')]
    return links