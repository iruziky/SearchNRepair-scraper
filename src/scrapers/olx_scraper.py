from playwright.sync_api import sync_playwright
from config import BASE_URL, USER_AGENT, HEADLESS

def get_page_content():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        context = browser.new_context(user_agent=USER_AGENT)
        page = context.new_page()
        page.goto(BASE_URL)
        html = page.content()
        browser.close()
        return html
