from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# 1. Chargement du Model lorsque le serveur démarre
model = joblib.load('src/house_model.pkl')

@app.get("/")
def home():
    return {"message": "Welcome to House Price Prediction API"}

@app.post("/predict")
def predict(data: dict):
    # Conversion des données reçues en DataFrame
    df = pd.DataFrame([data])
    
    # Prédiction
    prediction = model.predict(df)
    
    return {"predicted_price": float(prediction[0])}