import csv

def save_to_csv(links, path="links.csv"):
    with open(path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Link"])
        for link in links:
            writer.writerow([link])
