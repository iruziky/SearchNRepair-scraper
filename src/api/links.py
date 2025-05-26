from utils.helpers import log
import requests
from typing import List

def list_all():
    url = "https://olx-back-end.onrender.com/links/listAll"
    response = requests.get(url, timeout=10)
    return response.json()

def save_link(link: str) -> None:
    url = "https://olx-back-end.onrender.com/links/save"
    payload = {"url": link}
    response = requests.post(url, json=payload, timeout=10)

    log(f"Status code: {response.status_code}")
    log(f"Response body: {response.text}")

def save_links(links: List) -> None:
    url = "https://olx-back-end.onrender.com/links/saveList"
    payload = [{"url": link} for link in links]
    response = requests.post(url, json=payload, timeout=10)

    log(f"Status code: {response.status_code}")
    log(f"Response body: {response.text}")
