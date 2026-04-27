from src.data_preprocessing import clean_data, get_encoded_data
from src.train_model import train_and_save
import pandas as pd

# 1. Nettoyage des données
train = clean_data('data/train.csv')
test = clean_data('data/test.csv')

# 2. Conversion des textes en nombres
train_final, test_final = get_encoded_data(train, test)

# 3. Isolation de la Target (le prix)
X = train_final.drop('SalePrice', axis=1)
y = train_final['SalePrice']

# 4. Entraînement et sauvegarde
train_and_save(X, y)
