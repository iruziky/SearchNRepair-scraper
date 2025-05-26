USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
EXPECTED_ELEMENT_SEARCH_PAGE = ".olx-link.olx-link--caption.olx-link--main"

# Get from back-end
STATE = "rio-grande-do-norte"
STATE_ABBREVIATION = "rn"
CITY = "natal"

BASE_URL = f"https://www.olx.com.br/celulares/estado-{STATE_ABBREVIATION}/{STATE}/{CITY}?q=trincado&sf=1&o="

# Selenium
WAIT_TIMEOUT = 30

SELECTORS = {
    "title": "#description-title > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)",
    "price": ".olx-text--title-large",
    "category": ".ad__sc-2h9gkk-3",
    "brand": "div.ad__sc-2h9gkk-0:nth-child(2) > div:nth-child(2) > span:nth-child(2)",
    "model": "div.ad__sc-2h9gkk-0:nth-child(3) > div:nth-child(2) > span:nth-child(2)",
    "condition": "div.ad__sc-2h9gkk-0:nth-child(4) > div:nth-child(2) > span:nth-child(2)",
    "memory": "div.ad__sc-2h9gkk-0:nth-child(5) > div:nth-child(2) > span:nth-child(2)",
    "color": "div.ad__sc-2h9gkk-0:nth-child(6) > div:nth-child(2) > span:nth-child(2)",
    "batteryLife": "div.ad__sc-2h9gkk-0:nth-child(7) > div:nth-child(2) > span:nth-child(2)",
    "description": ".ad__sc-2mjlki-1",
}