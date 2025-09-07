from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# Load model and encoders
try:
    model = joblib.load("model.pkl")
    encoders = joblib.load("encoders.pkl")
except Exception as e:
    raise RuntimeError(f"Error loading model or encoders: {e}")

# FastAPI app
app = FastAPI(title="Shaunak's Goa Power Outage Predictor")

# Input schema for request body
class PowerOutageInput(BaseModel):
    Town_Name: str
    Substation: str
    Feeder_Name: str
    Rural_Urban: str
    No_of_Consumers: int

@app.get("/")
def root():
    return {"message": "Welcome to Goa Power Outage Prediction API 🚀"}

@app.post("/predict")
def predict_outage(data: PowerOutageInput):
    try:
        # Encode categorical inputs
        town_enc = encoders["town"].transform([data.Town_Name])[0]
        substation_enc = encoders["substation"].transform([data.Substation])[0]
        feeder_enc = encoders["feeder"].transform([data.Feeder_Name])[0]
        rural_urban_enc = encoders["rural_urban"].transform([data.Rural_Urban])[0]

        # Create feature DataFrame
        input_df = pd.DataFrame([{
            "Town_Enc": town_enc,
            "Substation_Enc": substation_enc,
            "Feeder_Enc": feeder_enc,
            "Rural_Urban_Enc": rural_urban_enc,
            "No_of_Consumers": data.No_of_Consumers
        }])

        # Predict
        prediction = model.predict(input_df)[0]
        result = "Long Outage (> 1 hour)" if prediction == 1 else "Short Outage (<= 1 hour)"

        return {"prediction": result}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))