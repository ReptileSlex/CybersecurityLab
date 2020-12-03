from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


links = []      # Iniciamos una lista vacía para guardar los links
url = "https://revistabyte.es/ciberseguridad/"
html_doc = urlopen(url).read()
Objetosoup = BeautifulSoup(html_doc, "html.parser")

# Se filtran por regex 2 palabras dentro de todo el link
for link in Objetosoup.findAll('a', attrs={'href': re.compile("phishing|malware|amenaza")}):
    links.append(link.get("href"))

if not links:
    print("No hay resultados")
else:
    for i in range(0, len(links), 2):  # Con paso 2 porque tiene un bug que repite los links 2 veces dentro de la lista
        print(links[i])
        LinkSoup = urlopen(links[i]).read()
        NuevoObjSoup = BeautifulSoup(LinkSoup, "html.parser")
        PrimerParrafo = NuevoObjSoup.body.p.text
        print(PrimerParrafo)

    """print(links[0])
    LinkSoup = urlopen(links[0]).read()
    NuevoObjSoup = BeautifulSoup(LinkSoup, "html.parser")
    PrimerParrafo = NuevoObjSoup.body.p.text
    print(PrimerParrafo)"""