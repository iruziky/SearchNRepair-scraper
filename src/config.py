USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
EXPECTED_ELEMENT_SEARCH_PAGE = ".olx-link.olx-link--caption.olx-link--main"

# Get from back-end
STATE = "rio-grande-do-norte"
STATE_ABBREVIATION = "rn"
CITY = "natal"

BASE_URL = f"https://www.olx.com.br/celulares/estado-{STATE_ABBREVIATION}/{STATE}/{CITY}?q=trincado&sf=1&o="

# Selenium
WAIT_TIMEOUT = 30
