# Importació de mòduls i llibreries necessàries.
from bs4 import BeautifulSoup
import requests

# Càrrega de dades.
url = "https://fiftyoutlet.com/es/es/hombre/bano"
page = requests.get(url)
soup = BeautifulSoup(page.content)

# Classe amb les dades que ens interessen.
class_with_data = "_1J8_boT6ctWvJph_YCWSkj I15oAOBDYUGxoD2P1E9A8"

rows = soup.body.find_all("div", {"class": class_with_data})

# Classe on apareix la marca.
brand_attr = "_1L9CQf_2VW_ARk32xW-XT8 _2Riwmks0sQPFSYoywALIJ3"
brands = []

# Iteració per trobar les marques.
for row in rows:
    spans = row.find_all("span", {"class": brand_attr})
    for span in spans:
        brands.append(span.text.replace("\n", "").replace(" ", ""))

# Fent aquest print veiem com ens retorna 36 elements,
# el que retorna la cerca a la pàgina.
# print(brand, len(brand))
