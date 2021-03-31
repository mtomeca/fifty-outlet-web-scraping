from bs4 import BeautifulSoup
import requests
import pandas as pd


def download_content(url):
    """
    Funció que descarrega el source code de la pàgina desitjada i retorna
    un objecte BeautifulSoup.

    :param url: URL de la pàgina de les quals es vol fer web scraping.
    :return: objecte BeautifulSoup que conté la informació de la pàgina
    desitjada.
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content,
                         features="html.parser")
    return soup


def store_info(soup_obj, data_cl, data_size_cl, brand_cl, name_cl,
               frstPrices_cl, currPrices_cl, colors_cl, sizes_cl):
    """
    Funció que emmagatzema la informació de la pàgina web escollida en un diccionari
    amb el format i l'organització desitjada.

    :param soup_obj: objecte BeautifulSoup amb la informació desitjada.
    :param data_cl: classe amb la gran majoria de les dades i classes a extreure.
    :param data_size_cl: classe existent en tots els productes que conté informació
    de les talles de cada producte.
    :param brand_cl: classe que conté la marca de cada producte.
    :param name_cl: classe que conté la descripció o nom de cada producte.
    :param frstPrices_cl: classe que conté el preu original de cada producte.
    :param currPrices_cl: classe que conté el preu actual de cada producte.
    :param colors_cl: classe que conté els colors disponibles de cada producte.
    :param sizes_cl: classe que conté les talles disponibles de cada producte.
    :return: diccionari amb l'identificador i els camps desitjats.
    """
    # Files amb la majoria de dades a extreure.
    data_rows = soup_obj.body.find_all("div",
                                   {"class": data_cl})

    # Inicialització del diccionari on s'emmagatzemaran les dades.
    data_dic = {}

    for id, row in enumerate(data_rows):
        id += 1
        # Llista on s'emmagatzemaran els colors de cada variable.
        color_list = []
        # Creem un diccionari per cada variable dins del diccionari inicial.
        data_dic[id] = {}

        # Definició dels elements que cal emmagatzemar.
        names = row.find_all("a", name_cl)
        brands = row.find_all("span", {"class": brand_cl})
        links = row.find_all("a", {"class": name_cl})
        firstPrices = row.find_all("span", {"class": frstPrices_cl})
        currentPrices = row.find_all("span", {"class": currPrices_cl})
        colors = row.find_all("a", {"class": colors_cl})

        # Emmagatzematge de les dades al diccionari.
        for brand in brands:
            data_dic[id]["Brand"] = brand.text.replace("\n", "").replace(" ", "")
        for name in names:
            data_dic[id]["Description"] = name.text
        for link in links:
            data_dic[id]["Link"] = link['href']
        for firstPrice in firstPrices:
            data_dic[id]["First Price"] = firstPrice.text
        for currPrice in currentPrices:
            data_dic[id]["Current Price"] = currPrice['data-price']
        for color in colors:
            color_list.append(color['title'])
        data_dic[id]["Color"] = color_list
        data_dic[id]["Colors available"] = len(color_list)

    # Classe on apareixen les talles de cada producte.
    sizes = soup_obj.body.find_all("div", {"class": data_size_cl})

    for id, size in enumerate(sizes):
        id += 1
        # Llista on s'emmagatzemen les talles de cada producte.
        size_list = []
        size_opt = size.find_all("button")

        for i in size_opt:
            # Si una talla està esgotada, no s'inclou al diccionari.
            if not i.has_attr('disabled'):
                size_list.append(i['data-size-id'])
        data_dic[id]["Sizes"] = size_list

    # Retorna el diccionari generat.
    return data_dic


def output(file_name, dic):
    """
    Funció que crea l'arxiu csv que conté el dataset generat amb
    el web scraping realitzat.

    :param file_name: nom que se li vol donar a l'arxiu.
    :param dic: diccionari que conté les dades extretes, producte de la funció
    store_info.
    :return: no retorna cap element, simplement genera el fitxer.
    """
    # Llista on s'emmagatzemaran els noms dels camps obtinguts.
    column_names = ["ID"]
    # Llista de línies que s'escriuran al fitxer. Serà una llista de llistes
    # que s'utilitzarà en la creació del dataframe que s'exportarà a csv.
    lines = []

    # Creació de les llistes (una per cada línia) que s'utilitzen en la creació
    # del dataframe.
    for id, inner_dic in dic.items():
        # Per cada ID, s'inicialitza la llista contenint només aquest element.
        line = [id]
        # S'afegeixen a la llista totes les variables que conté el diccionari.
        for field in inner_dic.keys():
            line.append(inner_dic[field])
            # Paral·lelament, es crea una llista amb els camps que s'utilitzarà
            # per definir la capçalera.
            if field not in column_names:
                column_names.append(field)
        # S'emmagatzema la línia completa abans de reinicialitzar la variable "line"
        # pel següent ID.
        lines.append(line)

    # Creació del dataframe amb la llibreria "pandas" que permet extreure el dataset
    # en format csv d'una manera senzilla.
    df = pd.DataFrame(
        lines,
        columns=column_names
    )

    # Exportació del dataset al fitxer csv amb el nom indicat.
    df.to_csv(file_name,
              index=False)
