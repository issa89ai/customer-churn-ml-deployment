import streamlit as st
import requests

st.set_page_config(page_title="Customer Churn Prediction", page_icon="📉", layout="centered")

st.title("📉 Customer Churn Prediction")
st.write("Enter customer details below to predict whether the customer is likely to churn.")

API_URL = "http://127.0.0.1:8000/predict"

age = st.number_input("Age", min_value=18, max_value=100, value=35)
gender = st.selectbox("Gender", ["Male", "Female"])
tenure = st.number_input("Tenure", min_value=0, max_value=100, value=12)
usage_frequency = st.number_input("Usage Frequency", min_value=0, max_value=100, value=15)
support_calls = st.number_input("Support Calls", min_value=0, max_value=50, value=2)
payment_delay = st.number_input("Payment Delay", min_value=0, max_value=100, value=5)
subscription_type = st.selectbox("Subscription Type", ["Basic", "Standard", "Premium"])
contract_length = st.selectbox("Contract Length", ["Monthly", "Quarterly", "Annual"])
total_spend = st.number_input("Total Spend", min_value=0.0, value=500.0, step=10.0)
last_interaction = st.number_input("Last Interaction", min_value=0, max_value=365, value=10)

if st.button("Predict"):
    payload = {
        "Age": age,
        "Gender": gender,
        "Tenure": tenure,
        "Usage_Frequency": usage_frequency,
        "Support_Calls": support_calls,
        "Payment_Delay": payment_delay,
        "Subscription_Type": subscription_type,
        "Contract_Length": contract_length,
        "Total_Spend": total_spend,
        "Last_Interaction": last_interaction,
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()

            if "error" in result:
                st.error(result["error"])
            else:
                st.success(f"Prediction: {result['result']}")
                st.write(f"**Prediction Code:** {result['prediction']}")
                st.write(f"**Churn Probability:** {result['churn_probability']}")
                st.write(f"**No Churn Probability:** {result['no_churn_probability']}")
        else:
            st.error(f"API Error: {response.status_code}")
            st.write(response.text)

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to FastAPI backend. Make sure the API is running on http://127.0.0.1:8000")