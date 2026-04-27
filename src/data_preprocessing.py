import pandas as pd

def clean_data(file_path):
    # Lecture des données
    df = pd.read_csv(file_path)
    
    # Suppression des colonnes avec trop de valeurs manquantes
    cols_to_drop = ['PoolQC', 'MiscFeature', 'Alley', 'Fence', 'MasVnrType', 'FireplaceQu']
    df = df.drop(columns=[c for c in cols_to_drop if c in df.columns])
    
    # Remplacement des valeurs manquantes selon le type de colonne
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].fillna('None')
        else:
            df[col] = df[col].fillna(0)
            
    return df

def get_encoded_data(train_df, test_df):
    # Conversion en Dummies et uniformisation des colonnes
    train_final = pd.get_dummies(train_df)
    test_final = pd.get_dummies(test_df)
    
    # Assurer que train et test ont les mêmes colonnes
    train_final, test_final = train_final.align(test_final, join='left', axis=1, fill_value=0)
    
    return train_final, test_final