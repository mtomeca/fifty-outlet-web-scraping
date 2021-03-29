# Importació de mòduls i llibreries necessàries.
from bs4 import BeautifulSoup
import requests
import selenium


# Càrrega de dades.
url = "https://fiftyoutlet.com/es/es/hombre/bano"
page = requests.get(url)
soup = BeautifulSoup(page.content)
#soup = BeautifulSoup(page.content, features="html.parser")


# Diccionari on s'emmagatzemen les dades.
data_dic = {}

# Classe amb les dades que ens interessen.
class_with_data = "_1J8_boT6ctWvJph_YCWSkj I15oAOBDYUGxoD2P1E9A8"

rows = soup.body.find_all("div", {"class": class_with_data})

# Classe on apareix la marca del producte.
brand_attr = "_1L9CQf_2VW_ARk32xW-XT8 _2Riwmks0sQPFSYoywALIJ3"

# Classe on apareix el nom i el link del producte.
name_attr = "link nJKI1osfGm1xE1PkAhWEJ _1rx5s5SBfiZyD0JhPp23hM"

# Classe on apareix el preu inicial del producte.
first_Price = "_306iTrToX_OShtSAP7XevK _1Y-4pH1BWwMV4UMjEhAG36"

# Un altre preu.
prices_class = "UsayrQmgXA1LiQJ2Isauz _2Tf_MA-3j5q-XdElDrZ64N"

# Classe on apareix e preu actual del producte.
curr_Price_class = "_2S2si9T7Qd3avRwavIc7Fo m8dZQhR-BlEOUvpj0ciDk" +\
                   " _35S_lNpYfl-bzhzNIldqTR JMJtx_uzL1tBgGN3qpKJf " +\
                   "js-product-price"

# Classe on apareix el color.
color_class = "undefined CkZqObjicR_F4ZOC7Hv3u selected"

# Classe amb les talles.
class_with_sizes = "_2gvZJbOD9AAqBnX5diXm5p js-size-selector"
sizes = soup.body.find_all("div", {"class": class_with_sizes})

# Camp que es defineix com a identificador o clau primària.
id = 0

# Iteració per emmagatzemar les dades.
for row in rows:
    id += 1
    color_list = []
    data_dic[id] = {}

    a_rows = row.find_all("a", name_attr)
    spans = row.find_all("span", {"class": brand_attr})
    links = row.find_all("a", {"class": name_attr})
    firstPrices = row.find_all("span", {"class": first_Price})
    currentPrices = row.find_all("span", {"class": curr_Price_class})
    colors = row.find_all("a", {"class": color_class})

    for span in spans:
        data_dic[id]["Brand"] = span.text.replace("\n", "").replace(" ", "")
    for a_row in a_rows:
        data_dic[id]["Description"] = a_row.text
    for link in links:
        data_dic[id]["Link"] = link['href']
    for firstPrice in firstPrices:
        data_dic[id]["First Price"] = firstPrice.text
    for currPrice in currentPrices:
        data_dic[id]["Current Price"] = currPrice['data-price']
    for color in colors:
        color_list.append(color['title'])
    data_dic[id]["Color"] = color_list


for id, size in enumerate(sizes):
    id += 1
    size_list = []
    size_opt = size.find_all("button")

    for i in size_opt:
        if not i.has_attr('disabled'):
            size_list.append(i['data-size-id'])
    data_dic[id]["Sizes"] = size_list
