# %%
import tensorflow as tf
import pandas as pd 
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn import preprocessing
from sklearn.semi_supervised import LabelPropagation
from sklearn.multioutput import MultiOutputClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
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
vectorizer = TfidfVectorizer()
X_labeled_vectorized = vectorizer.fit_transform(X_labeled)
# %%
# Créer le modèle de propagation de l'étiquette
model = MultiOutputClassifier(KNeighborsClassifier())
model.fit(X_labeled_vectorized, y_labeled)

# Prédire les étiquettes des données non labellisées
y_pred = model.predict(vectorizer.transform(unlabeled_data['avis']))

# %%
# Associez les étiquettes prédites aux données non labellisées
unlabeled_data[categories] = y_pred
# Concaténez les données labellisées et non labellisées
classified_data = pd.concat([labeled_data, unlabeled_data])
classified_data =classified_data.fillna(0)
# Affichez les résultats
print(classified_data)

unlabeled_data.to_excel(r"C:\Users\ramad\OneDrive - Université Paris-Dauphine\M2-IASD\NLP\NLP_airline\prediction.xlsx")
classified_data.to_excel(r"C:\Users\ramad\OneDrive - Université Paris-Dauphine\M2-IASD\NLP\NLP_airline\final_data.xlsx")
