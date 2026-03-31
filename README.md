README.md
# Customer Churn ML Deployment

A full machine learning deployment project for **Customer Churn Prediction** using:

- **scikit-learn** for model training
- **FastAPI** for backend API
- **Streamlit** for frontend user interface
- **Docker** for containerization

---

## Project Overview

This project predicts whether a customer is likely to **churn** or **not churn** based on customer-related features such as:

- Age
- Gender
- Tenure
- Usage Frequency
- Support Calls
- Payment Delay
- Subscription Type
- Contract Length
- Total Spend
- Last Interaction

The model is trained using a **Random Forest Classifier** and deployed through a FastAPI backend, with a Streamlit frontend for interactive predictions.

---

## Project Structure

```bash
customer_churn_ml_deployment/
├── app/
│   ├── main.py
│   ├── model_loader.py
│   └── schema.py
├── frontend/
│   └── streamlit_app.py
├── model/
│   ├── train_model.py
│   ├── churn_model.pkl
│   └── encoders.pkl
├── data/
│   └── customer_churn.csv
├── venv/
├── .dockerignore
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
Dataset

Dataset used:

data/customer_churn.csv

Target column:

Churn
0 = No Churn
1 = Churn
Model Training

The model training script:

python model/train_model.py

This script:

loads the dataset
cleans and preprocesses the data
encodes categorical features
trains a Random Forest Classifier
evaluates the model
saves:
model/churn_model.pkl
model/encoders.pkl
Model Performance

The trained model achieved very high accuracy on the dataset.

Example result:

Accuracy: ~0.9986
Important Note

This very high accuracy suggests the dataset is highly separable.
Feature importance analysis showed that Payment Delay is the strongest predictor, followed by:

Support Calls
Tenure
Usage Frequency

This means the model performs very well on this dataset, but real-world customer churn prediction may be more complex.

Feature Importance Insight

Top important features:

Payment Delay
Support Calls
Tenure
Usage Frequency
Gender

This helps explain why the model predicts churn effectively and also adds interpretability to the project.

FastAPI Backend

Run the backend from the project root:

python -m uvicorn app.main:app --reload

API will run at:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs
API Endpoints
Home
GET /
Prediction
POST /predict

Example JSON input:

{
  "Age": 35,
  "Gender": "Male",
  "Tenure": 12,
  "Usage_Frequency": 15,
  "Support_Calls": 2,
  "Payment_Delay": 5,
  "Subscription_Type": "Standard",
  "Contract_Length": "Annual",
  "Total_Spend": 500.0,
  "Last_Interaction": 10
}

Example response:

{
  "prediction": 0,
  "result": "No Churn",
  "churn_probability": 0.0,
  "no_churn_probability": 1.0
}
Streamlit Frontend

Run the frontend from the project root:

python -m streamlit run frontend/streamlit_app.py

The app will open in the browser, usually at:

http://localhost:8501

The frontend sends user input to the FastAPI backend and displays:

prediction result
prediction code
churn probability
no churn probability
Installation

Clone the repository and install dependencies:

git clone <your-repository-url>
cd customer_churn_ml_deployment
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Requirements

Main libraries used:

fastapi
uvicorn
streamlit
requests
pandas
scikit-learn
matplotlib
pydantic

Install them with:

python -m pip install -r requirements.txt
Docker

Build the Docker image:

docker build -t customer-churn-api .

Run the container:

docker run -p 8000:8000 customer-churn-api

Then open:

http://127.0.0.1:8000/docs
Note

This Dockerfile currently runs the FastAPI backend.
The Streamlit frontend is run separately on your local machine unless you later create a separate container for it.

Key Learning Outcomes

This project demonstrates:

classification model training
preprocessing categorical and numerical data
model serialization with pickle
API deployment using FastAPI
frontend-backend integration using Streamlit
containerization using Docker
Future Improvements

Possible next improvements:

improve frontend UI styling
add separate Docker setup for Streamlit
deploy online using Render, Railway, or Azure
add better probability formatting
test with additional datasets
check and reduce possible data leakage
Author

Ahmad
Master’s student in Computer Science
