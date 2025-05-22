from playwright.sync_api import sync_playwright
from src.config import BASE_URL

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Mostra o navegador para tentar passar pelo bloqueio
        context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
        page = context.new_page()
        page.goto(BASE_URL)
        print("Título da página:", page.title())
        browser.close()

if __name__ == "__main__":
    run()
