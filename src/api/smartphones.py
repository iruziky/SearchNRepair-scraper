from models.smartphone import Smartphone
from utils.helpers import log
from dataclasses import asdict
import requests

def save_smartphone(smartphone: Smartphone) -> None:
    url = "https://olx-back-end.onrender.com/smartphones/save"
    smartphone_dict = asdict(smartphone)
    response = requests.post(url, json=smartphone_dict, timeout=10)
    
    log(f"Status code: {response.status_code}")
    log(f"Response body: {response.text}")