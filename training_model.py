# %%
import tensorflow as tf
import pandas as pd 
import numpy as np
import sklearn
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn import preprocessing
from sklearn.semi_supervised import LabelPropagation
from sklearn.multioutput import MultiOutputClassifier
from sklearn.svm import SVC
from transformers import TFBertModel, BertTokenizer
# %%
df = pd.read_excel(r"C:\Users\ramad\OneDrive - Université Paris-Dauphine\M2-IASD\NLP\NLP_airline\airlines_reviews_preprocessed_labeled.xlsx", index_col=False)
df.shape
# %%
categories = [x for x in df.columns if x not in ['Unnamed: 0', 'note_globale', 'site', 'compagnie_aerienne', 'note',
       'avis', 'nouvel note']]

# %%
labeled_data = df.dropna(subset=categories, how="all")
unlabeled_data = df.drop(labeled_data.index)
print(labeled_data.shape)
print(unlabeled_data.shape)
# %%
# Séparer les caractéristiques (X) des étiquettes (y) pour les données labellisées
X_labeled = labeled_data['avis']
y_labeled = labeled_data[categories].fillna(0)
# %%
# Créer un vecteur TF-IDF pour représenter les données textuelles
vectorizer = CountVectorizer()
X_labeled_vectorized = vectorizer.fit_transform(X_labeled)
# %%
# Créer le modèle de propagation de l'étiquette
model = MultiOutputClassifier(SVC())
model.fit(X_labeled_vectorized, y_labeled)

# Prédire les étiquettes des données non labellisées
y_pred = model.predict(vectorizer.transform(unlabeled_data['avis']))

# %%
# Associez les étiquettes prédites aux données non labellisées
unlabeled_data[categories] = y_pred
# Concaténez les données labellisées et non labellisées
classified_data = pd.concat([labeled_data, unlabeled_data])

# Affichez les résultats
print(classified_data)

unlabeled_data.to_excel(r"C:\Users\ramad\OneDrive - Université Paris-Dauphine\M2-IASD\NLP\NLP_airline\prediction.xlsx")
classified_data.to_excel(r"C:\Users\ramad\OneDrive - Université Paris-Dauphine\M2-IASD\NLP\NLP_airline\final_data.xlsx")

#INSATISFAISANT
# tentative avec du préent
# %%

#####################################################################
data = {
    'avis': ['A1', 'A2', 'A3', 'A4', 'A5'],
    'cat1': [None, 1, 1, None, None],
    'cat2': [1, None, 1, None, None],
    'cat3': [None, None, None, None, None],
    'cat4': [1, 1, None, 1, None]
}
df = pd.DataFrame(data)

categories = ['cat1', 'cat2', 'cat3', 'cat4']

# Supprimer les lignes où toutes les colonnes correspondantes aux catégories sont nulles
df_filtered = df.dropna(subset=categories, how='all')

print(df_filtered)
#########################################################################

X = df_filtered['avis']
y = df[categories]
