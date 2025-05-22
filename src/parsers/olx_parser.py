from bs4 import BeautifulSoup
from models.listing import Listing

def parse_listings(html):
    soup = BeautifulSoup(html, 'html.parser')
    listings = []

    for item in soup.select("li.sc-1fcmfeb-2"):
        title = item.select_one("h2").get_text(strip=True) if item.select_one("h2") else "No title"
        price = item.select_one("p").get_text(strip=True) if item.select_one("p") else "No price"
        listings.append(Listing(title=title, price=price))

    return listings
