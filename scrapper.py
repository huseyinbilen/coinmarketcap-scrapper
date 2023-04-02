from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

table = soup.find("table", {"class": "sc-beb003d5-3 ieTeVa cmc-table"})

header = []
rows = []
for i, row in enumerate(table.find_all('tr')):
    if i == 0:
        header = [el.text.strip() for el in row.find_all('th')]
    else:
        rows.append([el.text.strip() for el in row.find_all('td')])

print(header)
for row in rows:
    print(row)