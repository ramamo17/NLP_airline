# %%
import re
import pandas as pd

# Exemple de DataFrame
df = pd.read_excel(r"C:\Users\ramad\OneDrive - Université Paris-Dauphine\M2-IASD\NLP\NLP_airline\df_2_dataset.xlsx")

# Fonction de prétraitement
def preprocess_text(text):
    # Remplacer les caractères accentués par leur équivalent non accentué
    text = re.sub(r'[éêèë]', 'e', text)
    text = re.sub(r'[ù]', 'u', text)
    text = re.sub(r'[à]', 'a', text)
    text = re.sub(r'[ç]', 'c', text)
    text = re.sub(r'[ïî]', 'i', text)
    text = re.sub(r'[ô]', 'o', text)
    
    # Retirer les virgules
    text = re.sub(r',', ' ', text)
    # Retirer les caractères spéciaux et les chiffres
    text = re.sub(r'[^a-zA-Z ]', ' ', text)
    # Mettre tout en minuscule
    text = text.lower()
    # Retirer les apostrophes
    text = re.sub(r"'", ' ', text)
    # Retirer les sauts de ligne et les tabulations
    text = re.sub(r'\n|\t', ' ', text)
    # Retirer les '\n'
    text = re.sub(r'\\n', ' ', text)
    # Supprimer les espaces consécutifs
    text = re.sub(r' +', ' ', text)
    # Tokenisation au niveau des espaces
    tokens = text.split()
    
    return tokens
# Appliquer la fonction de prétraitement à la colonne 'avis'
df['avis'] = df['avis'].apply(preprocess_text)

print(df)

# %%
#Tokeniser à chaque espace 