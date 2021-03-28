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

# Classe on apareix la marca del producte.
brand_attr = "_1L9CQf_2VW_ARk32xW-XT8 _2Riwmks0sQPFSYoywALIJ3"
brands = []
# Classe on apareix el nom del producte.
name_attr = "link nJKI1osfGm1xE1PkAhWEJ _1rx5s5SBfiZyD0JhPp23hM"
names = []

# Iteració per trobar les marques.
for row in rows:
    a_rows = row.find_all("a", name_attr)
    spans = row.find_all("span", {"class": brand_attr})
    for span in spans:
        brands.append(span.text.replace("\n", "").replace(" ", ""))
    for a_row in a_rows:
        names.append(a_row.text)

# Fent aquest print veiem com ens retorna els elements
# de la pàgina.
# print(brands, len(brands))

# Suposo que es van guardant per ordre i els índexs es corresponen entre les llistes, però podríem mirar
# de buscar algun id que ens servís per identificar cada producte.
# He vist que hi ha una part de javascript on s'hi especifiquen variables, però no he tingut temps a mirar-ho
# bé i no he pogut instal·lar selenium...
