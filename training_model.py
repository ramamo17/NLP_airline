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
classified_data.fillna(0)
# Affichez les résultats
print(classified_data)

unlabeled_data.to_excel(r"C:\Users\ramad\OneDrive - Université Paris-Dauphine\M2-IASD\NLP\NLP_airline\prediction.xlsx")
classified_data.to_excel(r"C:\Users\ramad\OneDrive - Université Paris-Dauphine\M2-IASD\NLP\NLP_airline\final_data.xlsx")

# INFERENCE
# %%
# on veut tester notre modèle

text_test = 'Les billets étaient vraiment trop chères je ne suis pas content'



# %%
#INSATISFAISANT
# tentative avec du préentrainé
model_name = 'bert-base-multilingual-cased'
tokenizer = BertTokenizer.from_pretrained(model_name)
bert_model = TFBertModel.from_pretrained(model_name)

# %%
# Tokenisation des textes
tokenized_texts = [tokenizer.tokenize(text) for text in X_labeled]

# Ajout des tokens spéciaux [CLS] et [SEP]
input_ids = [tokenizer.convert_tokens_to_ids(tokens) for tokens in tokenized_texts]
input_ids = tf.keras.preprocessing.sequence.pad_sequences(input_ids, padding='post')

# %%
# Masque d'attention
attention_mask = tf.where(X_labeled != 0, 1, 0)

# Couche d'entrée
input_layer = tf.keras.layers.Input(shape=(X_labeled.shape[1],), dtype=tf.int32)

# Couche d'attention
attention_layer = tf.keras.layers.Attention()([input_layer, attention_mask])

# Couche BERT
bert_output = bert_model(input_layer, attention_mask=attention_mask)[0]

# Couche de classification
output_layer = tf.keras.layers.Dense(units=4, activation='sigmoid')(bert_output)

# Création du modèle
model = tf.keras.models.Model(inputs=input_layer, outputs=output_layer)

# %%
# Compilation
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Préparation des données de sortie
output_data = [data['cat1'], data['cat2'], data['cat3'], data['cat4']]

# Entraînement
model.fit(input_ids, output_data, epochs=10, batch_size=16)




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
