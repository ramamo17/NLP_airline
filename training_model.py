# %%
import tensorflow as tf
import pandas as pd 
import numpy as np
import sklearn
import os


df = pd.read_excel(r"C:\Users\ramad\OneDrive - Université Paris-Dauphine\M2-IASD\NLP\NLP_airline\airlines_reviews_preprocessed_labeled.xlsx", index_col=False)
# %%
df.head()
# %%
