from bs4 import BeautifulSoup
import requests
import json

url = "https://coinmarketcap.com"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

table = soup.find("table", {"class": "sc-beb003d5-3 ieTeVa cmc-table"})

header = []
rows = []
data = []
for i, row in enumerate(table.find_all('tr')):
    if i == 0:
        header = [el.text.strip() for el in row.find_all('th')]
        del header[0]
        del header[0]
        del header[len(header)-1]
    else:
        rows.append([el.text.strip() for el in row.find_all('td')])

for row in rows:
    temp = {
        "name": row[2],
        "price": row[3]
    }
    data.append(temp)

with open('result.json', 'w') as fp:
    json.dump(data, fp)

print("JSON File Created!")