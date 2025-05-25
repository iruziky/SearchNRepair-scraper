import undetected_chromedriver as uc
from controllers.scraper_controller import search_page_scraper, products_scraper

def main():
    options = uc.ChromeOptions()
    options.headless = False
    
    driver = uc.Chrome(options=options)
    
    try:
        search_page_scraper(driver)
        #products_scraper(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()