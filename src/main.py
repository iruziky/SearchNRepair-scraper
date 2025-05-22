import undetected_chromedriver as uc
from controllers.scraper_controller import product_links_scraper, products_scraper

def main():
    # Configuração do driver
    options = uc.ChromeOptions()
    options.headless = False  # Ou True se quiser headless
    
    driver = uc.Chrome(options=options)
    
    try:
        product_links_scraper(driver)
        #products_scraper(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()