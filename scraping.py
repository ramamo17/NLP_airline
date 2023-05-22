# %%
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_avis_google(url):
    # Envoie une requête GET à l'URL donnée
    response = requests.get(url)
    
    # Vérifie si la requête a réussi
    if response.status_code == 200:
        # Utilise BeautifulSoup pour analyser le contenu HTML de la page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Trouve tous les éléments d'avis sur la page
        avis = soup.find_all('div', class_='review')
        
        # Parcours chaque avis et extrait les informations souhaitées
        for a in avis:
            note = a.find('span', class_='rating').text
            commentaire = a.find('span', class_='review-text').text
            print(f"Note : {note}")
            print(f"Commentaire : {commentaire}")
            print('---')
    else:
        print("Échec de la requête.")

# Appel de la fonction avec l'URL de la page des avis Google
scrape_avis_google('https://www.google.com/maps/place/Restaurant+Example/reviews')

