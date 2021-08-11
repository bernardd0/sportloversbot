import pandas as pd
import os

raiz_url = "https://brasil.elpais.com/resultados/deportivos/juegos-olimpicos/calendario/"
urls = {}

def url_general():
    for dia in range(21, 32):
        dia = "2021-07-"+str(dia)
        urls[dia] = raiz_urls + dia

    for dia in range(1, 9):
        dia = "2021-08-"+str(dia)
        urls[dia] = raiz_urls + dia

def data_extraction_per_url(dia, url):
    pd.read_html(url)[0].to_csv(os.path.join("data/", dia+".csv"))

def extraction_programming_complete():
    for (dia, url) in urls.items():
        data_extraction_per_url(dia, url)

