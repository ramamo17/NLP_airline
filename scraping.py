# %%
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
# %%
my_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
# url = "https://www.esky.fr/avis/al/ca/air-china?_gl=1*1kbp9r2*_up*MQ..*_ga*MTY5MjkwMjM3NC4xNjg0ODI4MTk0*_ga_C0RM0D546D*MTY4NDgyODE5NC4xLjAuMTY4NDgyODE5NC4wLjAuMA..*_ga_N9CRQD0ZQC*MTY4NDgyODE5NC4xLjAuMTY4NDgyODE5NC4wLjAuMA.."
# url = "https://fr.igraal.com/avis/Air-France"
url = "https://www.ebuyclub.com/avis/air-france-5612"
response = requests.get(url, headers=my_headers)

# %%
html_soup = BeautifulSoup(response.text, 'html.parser')
# %%
reviews = html_soup.find_all("p", class_="avis-texte")
# %%
compagnie_element = html_soup.find('span', class_='bold uppercase')
compagnie_aerienne = compagnie_element.text.strip() if compagnie_element else None

avis_elements = html_soup.find_all('p', class_='avis-texte')
avis = [element.text for element in avis_elements]

notes_elements = html_soup.find_all('span', class_='note')
notes = [float(element.meta['content']) for element in notes_elements]

notes_elements = html_soup.find_all('meta', itemprop='ratingValue')
toutes_notes = [float(element['content']) for element in notes_elements]
note_globale = toutes_notes[0]
notes = toutes_notes[1:]

data = {
    'compagnie': [compagnie_aerienne] * len(avis),
    'avis': avis,
    'note': notes
}

df = pd.DataFrame(data)


# %%
# ebuyclub.com
urls = [
    "https://www.ebuyclub.com/avis/air-france-5612",
    "https://www.ebuyclub.com/avis/iberia-7119",
    "https://www.ebuyclub.com/avis/lufthansa-3420",
    "https://www.ebuyclub.com/avis/vueling-948",
    "https://www.ebuyclub.com/avis/emirates-1249",
    "https://www.ebuyclub.com/avis/air-corsica-2503",
    "https://www.ebuyclub.com/avis/ryanair-7076",
    "https://www.ebuyclub.com/avis/turkishairlines-5647",
    "https://www.ebuyclub.com/avis/singapore-airlines-8793",
    "https://www.ebuyclub.com/avis/brussels-airlines-2502",
    "https://www.ebuyclub.com/avis/air-serbia-12145",
    "https://www.ebuyclub.com/avis/british-airways-1436",
]
# DataFrame initial (vide)
df = pd.DataFrame(columns=['note_globale', 'compagnie_aerienne', 'avis', 'note'])

for url in urls:
    response = requests.get(url)
    html_soup = BeautifulSoup(response.content, 'html.parser')

    # # Extraction des données
    # compagnie_element = soup.find('span', class_='bold uppercase')
    # compagnie_aerienne = compagnie_element.text.strip() if compagnie_element else None

    # avis_elements = soup.find_all('p', class_='avis-texte')
    # avis = [element.text for element in avis_elements]

    # notes_elements = soup.find_all('meta', itemprop='ratingValue')
    # notes = [float(element['content']) for element in notes_elements]
    # Utilisation d'une expression régulière pour extraire le nom du site
    pattern = r"https?://(?:www\.)?([^/?]+)"
    match = re.search(pattern, url)
    nom_site = match.group(1)
    
    compagnie_element = html_soup.find('span', class_='bold uppercase')
    compagnie_aerienne = compagnie_element.text.strip() if compagnie_element else None

    avis_elements = html_soup.find_all('p', class_='avis-texte')
    avis = [element.text for element in avis_elements]

    notes_elements = html_soup.find_all('meta', itemprop='ratingValue')
    toutes_notes = [float(element['content']) for element in notes_elements]
    note_globale = toutes_notes[0]
    notes = toutes_notes[1:]

    # Création du DataFrame temporaire pour les données de l'URL actuelle
    data = {
        'site' : [nom_site]*len(avis),
        'compagnie_aerienne': [compagnie_aerienne] * len(avis),
        'avis': avis,
        'note': notes,
        'note_globale' : [note_globale]*len(avis)
    }
    df_temp = pd.DataFrame(data)

    # Concaténation du DataFrame temporaire avec le DataFrame principal
    df = pd.concat([df, df_temp], ignore_index=True)

# Affichage du DataFrame final
print(df)

# %%

urls = []
for i in range(1,14):
    urls.append(f"https://fr.custplace.com/air-france?page={i}")

for url in urls:
    response = requests.get(url)
    html_soup = BeautifulSoup(response.content, 'html.parser')

    # # Extraction des données
    # compagnie_element = soup.find('span', class_='bold uppercase')
    # compagnie_aerienne = compagnie_element.text.strip() if compagnie_element else None

    # avis_elements = soup.find_all('p', class_='avis-texte')
    # avis = [element.text for element in avis_elements]

    # notes_elements = soup.find_all('meta', itemprop='ratingValue')
    # notes = [float(element['content']) for element in notes_elements]
    # Utilisation d'une expression régulière pour extraire le nom du site
    pattern = r"https?://(?:www\.)?([^/?]+)"
    match = re.search(pattern, url)
    nom_site = match.group(1)
    
    #nom compagnie aérienne
    pattern_compagnie = r"https://fr\.custplace\.com/|\?page=\d*"
    compagnie_aerienne = re.sub(pattern_compagnie, "", str)
    
    #notes de chaque commentaire
    # notes_elements = html_soup.find_all('div', class_=['inline-block', 'mr-1.5', 'mb-2', 'aggregateRating'])
    # notes = [element['class'][-1][-1] for element in notes_elements]
    # notes = [x for x in notes if x.isdigit()]
    
    #commentaires
    avis_elements = html_soup.find_all('p', class_='mb-3')
    avis = [element.text for element in avis_elements]

    # la note moyenne de la compagnie sur le site
    note_globale = html_soup.select('span', class_=["text-lg", "xs:text-xl", "md:text-xxl", "font-medium"])

    # Création du DataFrame temporaire pour les données de l'URL actuelle
    data = {
        'site' : [nom_site]*len(avis),
        'compagnie_aerienne': [compagnie_aerienne] * len(avis),
        'avis': avis,
        'note': '0', #notes,
        'note_globale' : '0', #[note_globale]*len(avis)
    }
    df_temp = pd.DataFrame(data)

    # Concaténation du DataFrame temporaire avec le DataFrame principal
    df = pd.concat([df, df_temp], ignore_index=True)

# Affichage du DataFrame final
print(df)


# %%
#Luftansa
urls = ["https://www.poulpeo.com/avis/lufthansa.htm",
"https://www.poulpeo.com/avis/emirates.htm",
"https://www.poulpeo.com/avis/air-caraibes.htm",
"https://www.poulpeo.com/avis/vueling.htm", 
"https://www.poulpeo.com/avis/qatar-airways.htm",
"https://www.poulpeo.com/avis/tap-portugal-fr.htm",
"https://www.poulpeo.com/avis/air-france.htm"]

for url in urls:
    response = requests.get(url)
    html_soup = BeautifulSoup(response.content, 'html.parser')

    # # Extraction des données
    # compagnie_element = soup.find('span', class_='bold uppercase')
    # compagnie_aerienne = compagnie_element.text.strip() if compagnie_element else None


    # notes_elements = soup.find_all('meta', itemprop='ratingValue')
    # notes = [float(element['content']) for element in notes_elements]
    # Utilisation d'une expression régulière pour extraire le nom du site
    pattern = r"https?://(?:www\.)?([^/?]+)"
    match = re.search(pattern, url)
    nom_site = match.group(1)
    
    #nom compagnie aérienne
    # pattern_compagnie = r"https://fr\.custplace\.com/|\?page=\d*"
    pattern_compagnie = r"https://www\.poulpeo\.com/avis/|\.htm$"
    compagnie_aerienne = re.sub(pattern_compagnie, "", str)
    #notes de chaque commentaire
    # notes_elements = html_soup.find_all('div', class_=['inline-block', 'mr-1.5', 'mb-2', 'aggregateRating'])
    # notes = [element['class'][-1][-1] for element in notes_elements]
    # notes = [x for x in notes if x.isdigit()]
    
    #commentaires
    avis_elements = html_soup.find_all('div', class_='review-content')
    avis = [element.text for element in avis_elements]

    # # la note moyenne de la compagnie sur le site
    # note_globale = html_soup.select('span', class_=["text-lg", "xs:text-xl", "md:text-xxl", "font-medium"])

    # Création du DataFrame temporaire pour les données de l'URL actuelle
    data = {
        'site' : [nom_site]*len(avis),
        'compagnie_aerienne': [compagnie_aerienne] * len(avis),
        'avis': avis,
        'note': '0', #notes,
        'note_globale' : '0', #[note_globale]*len(avis)
    }
    df_temp = pd.DataFrame(data)

    # Concaténation du DataFrame temporaire avec le DataFrame principal
    df = pd.concat([df, df_temp], ignore_index=True)

# Affichage du DataFrame final
print(df)

df.to_excel(r"df_2_dataset.xlsx")
# %%
