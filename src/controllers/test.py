import requests

url = 'https://olx-back-end.onrender.com/smartphones/save' 
headers = {
    'Content-Type': 'application/json'
}
data = {"link": "https://rn.olx.com.br/rio-grande-do-norte/celulares/iphone-15-pro-max-256gb-natural-traseira-trincada-sem-defeitos-1400528659", "title": "iPhone 15 Pro Max 256GB Natural traseira trincada sem defeitos", "price": "R$ 5.999", "category": "Celulares E Smartphones", "brand": "Apple", "model": "Iphone 15 Pro Max", "condition": "Usado - Excelente", "memory": "256gb", "color": "Cinza", "batteryLife": "Perfeita (95% At\u00e9 100%)", "description": "Aparelho todo original nunca aberto, trinco fio de cabelo na traseira no cantinho direito, tela sem trincos, somente pel\u00edcula trincada remove na hora!\n\nSomente traseira trincada no cantinho, n\u00e3o dar pra sentir os trincos, tela sem trincos, repito tela sem trincos\n\n256GB ?\nFace ID ok \nSa\u00fade da bateria 99%\nSem entrada pra chip\nS\u00f3 pega chip virtual \n\nAceito todos os cart\u00f5es com acr\u00e9scimo negocio valor avista troco com volta do interessado", "images": "https://img.olx.com.br/images/90/908504649992384.jpg;https://img.olx.com.br/images/90/901530400953592.jpg;https://img.olx.com.br/images/10/101510161697360.jpg;https://img.olx.com.br/images/90/902544641216023.jpg;https://img.olx.com.br/images/90/908537164751045.jpg;", "isBreak": False}

response = requests.post(url, json=data, headers=headers)

print(response.status_code)
print(response.text)