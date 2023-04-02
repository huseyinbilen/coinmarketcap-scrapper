from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

print(soup)
