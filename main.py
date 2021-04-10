from functions import download_content, store_info, output
from selenium import webdriver

url_to_scrap = "https://fiftyoutlet.com/es/es/hombre/bano?sz=96"

soup = download_content(url_to_scrap)

# Classe amb les dades que ens interessen.
data_cl = "_1J8_boT6ctWvJph_YCWSkj I15oAOBDYUGxoD2P1E9A8"

# Classe on apareix la marca del producte.
brand_cl = "_1L9CQf_2VW_ARk32xW-XT8 _2Riwmks0sQPFSYoywALIJ3"

# Classe on apareix el nom i el link del producte.
name_cl = "link nJKI1osfGm1xE1PkAhWEJ _1rx5s5SBfiZyD0JhPp23hM"

# Classe on apareix el preu inicial del producte.
frstPrices_cl = "_306iTrToX_OShtSAP7XevK _1Y-4pH1BWwMV4UMjEhAG36"

# Classe on apareix e preu actual del producte.
currPrices_cl = "_2S2si9T7Qd3avRwavIc7Fo m8dZQhR-BlEOUvpj0ciDk" +\
                   " _35S_lNpYfl-bzhzNIldqTR JMJtx_uzL1tBgGN3qpKJf " +\
                   "js-product-price"

# Classe on apareix el color.
colors_cl = "undefined CkZqObjicR_F4ZOC7Hv3u selected"

# Classe amb les talles.
data_size_cl = "_2gvZJbOD9AAqBnX5diXm5p js-size-selector"

# Classe amb les talles.
sizes_cl = "_2gvZJbOD9AAqBnX5diXm5p js-size-selector"

dict_with_data = store_info(soup, data_cl, data_size_cl, brand_cl,
                            name_cl, frstPrices_cl, currPrices_cl, colors_cl, sizes_cl)


output("dataset.csv", dict_with_data)
print("Arxiu .csv creat correctament")
