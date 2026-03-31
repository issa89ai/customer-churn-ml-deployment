from fastapi import FastAPI
import pandas as pd

from app.schema import CustomerData
from app.model_loader import load_model, load_encoders

app = FastAPI(title="Customer Churn Prediction API")

model = load_model()
encoders = load_encoders()


@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API is running!"}


@app.post("/predict")
def predict(data: CustomerData):
    input_data = {
        "Age": data.Age,
        "Gender": data.Gender,
        "Tenure": data.Tenure,
        "Usage Frequency": data.Usage_Frequency,
        "Support Calls": data.Support_Calls,
        "Payment Delay": data.Payment_Delay,
        "Subscription Type": data.Subscription_Type,
        "Contract Length": data.Contract_Length,
        "Total Spend": data.Total_Spend,
        "Last Interaction": data.Last_Interaction,
    }

    df = pd.DataFrame([input_data])

    categorical_cols = ["Gender", "Subscription Type", "Contract Length"]

    for col in categorical_cols:
        if col in encoders:
            try:
                df[col] = encoders[col].transform(df[col])
            except ValueError:
                return {
                    "error": f"Invalid value '{df[col].iloc[0]}' for column '{col}'. Allowed values: {list(encoders[col].classes_)}"
                }

    prediction = model.predict(df)[0]
    prediction_proba = model.predict_proba(df)[0]

    churn_probability = float(prediction_proba[1])
    no_churn_probability = float(prediction_proba[0])

    result = "Churn" if prediction == 1 else "No Churn"

    return {
        "prediction": int(prediction),
        "result": result,
        "churn_probability": round(churn_probability, 4),
        "no_churn_probability": round(no_churn_probability, 4),
    }