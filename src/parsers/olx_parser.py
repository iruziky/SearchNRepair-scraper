def extract_links(page):
    tag_links = page.query_selector_all('a.olx-adcard__link')
    links = [link.get_attribute('href') for link in tag_links if link.get_attribute('href')]
    return links