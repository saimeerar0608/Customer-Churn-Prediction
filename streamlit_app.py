import streamlit as st
import joblib
import os
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# Load model
model = joblib.load("churn_model.pkl")

# Title
st.title("📊 Customer Churn Prediction Dashboard")
st.write("Customer Retention Risk Assessment System")

# Form Inputs
gender = st.selectbox("Gender", ["Female", "Male"])
senior = st.selectbox("Senior Citizen", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["No", "Yes"])

tenure = st.number_input("Tenure", min_value=0)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One Year", "Two Year"]
)

payment = st.selectbox(
    "Payment Method",
    ["Bank Transfer", "Credit Card", "Electronic Check", "Mailed Check"]
)

monthly = st.number_input("Monthly Charges", min_value=0.0)
total = st.number_input("Total Charges", min_value=0.0)

# Convert values
gender = 1 if gender == "Male" else 0
senior = 1 if senior == "Yes" else 0
dependents = 1 if dependents == "Yes" else 0

contract_map = {
    "Month-to-month": 0,
    "One Year": 1,
    "Two Year": 2
}

payment_map = {
    "Bank Transfer": 0,
    "Credit Card": 1,
    "Electronic Check": 2,
    "Mailed Check": 3
}

# Predict button
if st.button("Predict Customer Status"):

    features = [
        gender,
        senior,
        dependents,
        tenure,
        0,  # PhoneService
        0,  # MultipleLines
        0,  # InternetService
        0,  # OnlineSecurity
        0,  # OnlineBackup
        0,  # StreamingTV
        0,  # StreamingMovies
        contract_map[contract],
        payment_map[payment],
        monthly,
        total
    ]

    prediction = model.predict([features])

    if prediction[0] == 1:
        st.error("❌ CUSTOMER WILL CHURN")
        st.write("Accuracy: 84.72%")
        st.progress(82)
        st.warning("🏆 HIGH RISK CUSTOMER")
    else:
        st.success("✅ CUSTOMER WILL STAY")
        st.write("Accuracy: 84.72%")
        st.progress(18)