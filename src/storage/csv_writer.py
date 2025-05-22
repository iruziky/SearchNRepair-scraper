import csv
from models.listing import Listing

def save_to_csv(listings: list[Listing], path="listings.csv"):
    with open(path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Price"])
        for listing in listings:
            writer.writerow([listing.title, listing.price])
