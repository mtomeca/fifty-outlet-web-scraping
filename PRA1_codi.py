# Importació de mòduls i llibreries necessàries.
from bs4 import BeautifulSoup
import requests
import selenium

# Càrrega de dades.
url = "https://fiftyoutlet.com/es/es/hombre/bano"
page = requests.get(url)
soup = BeautifulSoup(page.content, features="html.parser")

# Classe amb les dades que ens interessen.
class_with_data = "_1J8_boT6ctWvJph_YCWSkj I15oAOBDYUGxoD2P1E9A8"

rows = soup.body.find_all("div", {"class": class_with_data})

# Classe on apareix la marca del producte.
brand_attr = "_1L9CQf_2VW_ARk32xW-XT8 _2Riwmks0sQPFSYoywALIJ3"
brands = []
# Classe on apareix el nom i el link del producte.
name_attr = "link nJKI1osfGm1xE1PkAhWEJ _1rx5s5SBfiZyD0JhPp23hM"
names = []
links_list = []

# Classe on apareix el preu inicial del producte.
first_Price = "_306iTrToX_OShtSAP7XevK _1Y-4pH1BWwMV4UMjEhAG36"
firstPrice_list = []


# Iteració per trobar les marques.
for row in rows:
    a_rows = row.find_all("a", name_attr)
    spans = row.find_all("span", {"class": brand_attr})
    links = row.find_all("a", {"class": name_attr})
    firstPrices = row.find_all("span", {"class": first_Price})
    for span in spans:
        brands.append(span.text.replace("\n", "").replace(" ", ""))
    for a_row in a_rows:
        names.append(a_row.text)
    for link in links:
        links_list.append(link['href'])
    for firstPrice in firstPrices:
        firstPrice_list.append(firstPrice.text)
        

car_price = row.find(class_ = "UsayrQmgXA1LiQJ2Isauz _2Tf_MA-3j5q-XdElDrZ64N").text.strip()

# Fent aquest print veiem com ens retorna els elements
# de la pàgina.
# print(f"Les marques són:\n{brands, len(brands)}")
# print(names)
# print(links_list)
print(firstPrice_list, len(firstPrice_list))
# print(rows[3])


# Suposo que es van guardant per ordre i els índexs es corresponen entre les llistes, però podríem mirar
# de buscar algun id que ens servís per identificar cada producte.


# He vist que hi ha una part de javascript on s'hi especifiquen variables, però no he tingut temps a mirar-ho
# bé i no he pogut instal·lar selenium...
