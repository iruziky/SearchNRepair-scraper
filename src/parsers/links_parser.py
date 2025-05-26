from api.links import list_all

def validate_links(links):
    scraping_links = list_all()
    filtered_links = links.copy()

    for target_url in reversed(links):
        exists = any(link["url"] == target_url for link in scraping_links)
        if exists:
            filtered_links.remove(target_url)

    return filtered_links