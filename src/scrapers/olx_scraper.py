from playwright.sync_api import sync_playwright
from config import BASE_URL, USER_AGENT, HEADLESS

def get_page(p):
    browser = p.chromium.launch(headless=HEADLESS)
    context = browser.new_context(user_agent=USER_AGENT)
    page = context.new_page()
    page.goto(BASE_URL)
    page.wait_for_selector(".olx-link.olx-link--caption.olx-link--main", timeout=30000)
    return browser, page

def next_page(page, index):
    page.goto(BASE_URL + "?o=" + str(index))

def is_last_page(page):
    text = page.inner_text("body")
    return "Ops! Nenhum anúncio foi encontrado." in text