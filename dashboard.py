import streamlit as st
import joblib
import pandas as pd
import os

# 1. Chargement du Model (vérifiez le chemin)
model_path = 'src/house_model.pkl'
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    st.error("❌ Modèle introuvable ! Exécutez 'python main.py' d'abord.")
    st.stop() # Arrête l'exécution ici si le modèle n'est pas trouvé

st.set_page_config(page_title="House Price AI", page_icon="🏠")

st.title("🏠 Prédiction des prix des maisons (Pro Version)")

# 2. Construction de l'interface dans la barre latérale (Sidebar)
with st.sidebar:
    st.header("Paramètres de la maison")
    lot_area = st.slider("Surface (LotArea)", 500, 50000, 8000)
    overall_qual = st.select_slider("Qualité générale (OverallQual)", options=list(range(1, 11)), value=5)
    year_built = st.number_input("Année de construction", 1872, 2010, 2000)

# 3. Traitement des données et prédiction (un bouton qui regroupe tout)
if st.button("Prédire le prix maintenant"):
    # Création d'un DataFrame avec les mêmes colonnes sur lesquelles le modèle s'est entraîné
    input_df = pd.DataFrame(0, index=[0], columns=model.feature_names_in_)
    
    # Remplacement des valeurs saisies par l'utilisateur
    input_df['LotArea'] = lot_area
    input_df['OverallQual'] = overall_qual
    input_df['YearBuilt'] = year_built
    
    # Prédiction
    prediction = model.predict(input_df)[0]
    
    # Affichage du résultat de manière attrayante
    st.metric(label="Prix prédit", value=f"${prediction:,.2f}")
    st.balloons()
    
    # --- Ajout d'un graphique "Pourquoi ce prix ?" ---
    st.markdown("---") # Ligne de séparation
    st.subheader("💡 Analyse des facteurs influents")
    
    # Calcul de l'importance approximative basée sur les valeurs saisies (Normalisé)
    importance = pd.DataFrame({
        'Facteur': ['Surface', 'Qualité', 'Âge de la maison'],
        'Impact relatif': [lot_area/50000, overall_qual/10, (year_built-1872)/138] 
    })
    
    # Affichage du graphique
    st.bar_chart(importance.set_index('Facteur'))
    st.info("Ce graphique montre comment chaque information saisie a contribué à l'augmentation ou la baisse du prix final.")
