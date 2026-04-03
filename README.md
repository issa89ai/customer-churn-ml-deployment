# 📉 Customer Churn ML Deployment

An end-to-end Machine Learning application that predicts customer churn using a Random Forest model.  
The system is fully deployed with a FastAPI backend and a Streamlit frontend.

---

## 🚀 Live Demo

## Live Demo

- Frontend App: https://customer-churn-ml-deployment-krqepa7ohqdqubyfcdp9ks.streamlit.app
- API Docs: https://customer-churn-api-njr0.onrender.com/docs
- API Base URL: https://customer-churn-api-njr0.onrender.com

---

## 📌 Project Overview

Customer churn prediction is a critical task for businesses to retain customers.  
This project predicts whether a customer will churn based on behavioral and demographic features.

---

## 🧠 Features Used

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

---

## ⚙️ Tech Stack

- **Machine Learning:** Scikit-learn (Random Forest)  
- **Backend API:** FastAPI  
- **Frontend UI:** Streamlit  
- **Deployment:** Render (API) + Streamlit Cloud (Frontend)  
- **Containerization:** Docker  

---

## 🏗️ Project Structure
customer-churn-ml-deployment/
│
├── app/ # FastAPI backend
├── frontend/ # Streamlit app
├── model/ # Trained model
├── data/ # Dataset
├── Dockerfile
├── requirements.txt
└── README.md


---

## 🔄 How It Works

1. User enters data in the Streamlit app  
2. Streamlit sends request to FastAPI API  
3. API loads trained model  
4. Model predicts churn probability  
5. Result is returned and displayed  

---

## 📸 Screenshots

### 🔹 API (Swagger UI)
![Swagger UI](assets/swagger_ui.png)

### 🔹 API Prediction Result
![Swagger Result](assets/swagger_result.png)

### 🔹 Streamlit Interface
![Streamlit UI](assets/streamlit_ui.png)

### 🔹 Streamlit Prediction
![Streamlit Result](assets/streamlit_result.png)

---

## 🎯 Key Highlights

- End-to-end ML pipeline  
- Real-time prediction via API  
- Fully deployed and publicly accessible  
- Clean separation between frontend and backend  

---

Ahmad Issa
Master’s in Computer Science
Focus: Data Science / Machine Learning / Applied AI
