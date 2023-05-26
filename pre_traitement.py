# %%
import re
import pandas as pd
from collections import Counter

# df = pd.read_excel(r"C:\Users\ramad\OneDrive - Université Paris-Dauphine\M2-IASD\NLP\NLP_airline\df_2_dataset_labeled.xlsx")
df = pd.read_excel(r"C:\Users\ramad\OneDrive - Université Paris-Dauphine\M2-IASD\NLP\NLP_airline\df_2_dataset.xlsx")

# Fonction de prétraitement
def preprocess_text(text, tokenize=True):
    """_summary_

    Args:
        text (_type_): _description_

    Returns:
        _list_of_string_: _tokenised and preprocessed text_
    """
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
    if tokenize:
        # Tokenisation au niveau des espaces
        tokens = text.split()
        # Supprimer les mots de longueur inférieure à 2
        tokens = [token for token in tokens if len(token) >= 3]
        return tokens
    else:
        return text
# Appliquer la fonction de prétraitement à la colonne 'avis'
df['avis'] = df['avis'].apply(preprocess_text)
df['compagnie_aerienne'] = df['compagnie_aerienne'].apply(preprocess_text,args=[False])
print(df)

# %%
#StopWords
def get_top_words(dataframe, text_column, num_words=50):
    """
    Renvoie une liste des mots les plus fréquents dans une colonne texte d'un DataFrame.
    
    Arguments :
    - dataframe : DataFrame - Le DataFrame contenant la colonne texte.
    - text_column : str - Le nom de la colonne texte.
    - num_words : int - Le nombre de mots à renvoyer (par défaut : 50).
    
    Retourne :
    - list - Une liste des mots les plus fréquents par ordre croissant d'apparition.
    """
    word_counts = Counter()
    
    for text in dataframe[text_column]:
        word_counts.update(text)
    
    top_words = [word for word, count in word_counts.most_common(num_words)]
    
    return top_words

top_words_list = get_top_words(df, "avis", num_words=100)
print(top_words_list)

# %% tri à la main des stopwords
stop_words = [x for x in top_words_list if x not in ['air', 'france', 'service', 'site', 'ete', 'bien', 'prix', 'sans', 'billet', 'avion', 'billets', 'voyage', 'vols', 'retour', 'reservation', 'paris', 'client', 'aller', 'bagages', 'bagage', 'recommande', 'personnel', 'jours', 'remboursement', 'aerienne', 'demande', 'euros', 'aeroport', 'achat', 'carte', 'bon', 'retard', 'heure', 'aucun', 'mois', 'clients', 'cool']]
# %%
# Filtrer les stopwords
def remove_stopwords_from_dataframe(dataframe, stop_words, text_column):
    """
    Supprime les mots de la liste stop_words d'une colonne texte d'un DataFrame.
    
    Arguments :
    - dataframe : DataFrame - Le DataFrame contenant la colonne texte.
    - stop_words : list - La liste des mots à supprimer.
    - text_column : str - Le nom de la colonne texte.
    
    Retourne :
    - DataFrame - Le DataFrame avec les mots stop_words supprimés de la colonne texte.
    """
    df_copy = dataframe.copy()
    
    def remove_stopwords_from_text(tokens):
        """
        Supprime les mots de la liste stop_words d'une liste de tokens.
        
        Arguments :
        - tokens : list - La liste de tokens.
        
        Retourne :
        - list - La liste de tokens sans les mots stop_words.
        """
        filtered_tokens = [token for token in tokens if token not in stop_words]
        return filtered_tokens
    
    df_copy[text_column] = df_copy[text_column].apply(remove_stopwords_from_text)
    
    return df_copy

df_without_stopwords = remove_stopwords_from_dataframe(df, stop_words, "avis")
print(df_without_stopwords)
# %%
import pandas as pd

def apply_stemming(dataframe, text_column):
    """
    Applique la fonction de stemming à une colonne texte d'un DataFrame.
    
    Arguments :
    - dataframe : DataFrame - Le DataFrame contenant la colonne texte.
    - text_column : str - Le nom de la colonne texte.
    
    Retourne :
    - DataFrame - Le DataFrame avec le stemming appliqué à la colonne texte.
    """
    df_copy = dataframe.copy()
    
    def stem_word(word):
        """
        Réduit un mot à sa forme de base en utilisant des règles de remplacement de suffixes.
        
        Arguments :
        - word : str - Le mot à réduire.
        
        Retourne :
        - str - Le mot réduit à sa forme de base.
        """
        suffixes = {
            "ance": "",
            "ence": "",
            "ité": "",
            "ment": "",
            "ant": "",
            "ent": "",
            "aux": "al",
            "eux": "eux",
            "e": "",
            "s": "",
        }
        
        for suffix, replacement in suffixes.items():
            if word.endswith(suffix):
                return word[:-len(suffix)] + replacement
        
        return word
    
    df_copy[text_column] = df_copy[text_column].apply(lambda tokens: [stem_word(token) for token in tokens])
    
    return df_copy

df_with_stemming = apply_stemming(df_without_stopwords, "avis")
print(df_with_stemming)

# %%
# sauvegarde 
df_with_stemming.reset_index(drop=True, inplace=True)
df_with_stemming.to_excel(r'C:\Users\ramad\OneDrive - Université Paris-Dauphine\M2-IASD\NLP\NLP_airline\airlines_reviews_preprocessed_labeled.xlsx', index=False)

# %%
