import random
import time
from datetime import datetime

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

def random_delay(min_seconds=1, max_seconds=3):
    time.sleep(random.uniform(min_seconds, max_seconds))
    
def wait(seconds: float):
    log(f"Aguardando {seconds:.2f} segundos antes de continuar...")
    time.sleep(seconds)
