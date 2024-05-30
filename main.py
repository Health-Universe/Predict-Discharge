import streamlit as st

# Title and description
st.title("Hospital Discharge Classification App")
st.write("""
### Welcome to the Hospital Discharge Classification App
This application helps hospitalists classify patients into two categories: 
1. Will discharge today.
2. Will not discharge today.
The classification is based on evidence-based features and a simple rule-based model.
""")

# User inputs
age = st.number_input("Patient Age", min_value=0, max_value=120, value=65)
length_of_stay = st.number_input("Current Length of Stay (days)", min_value=0, value=5)
comorbidities = st.number_input("Number of Comorbidities", min_value=0, max_value=10, value=2)
mobility = st.radio("Patient Mobility", ("Fully mobile", "Partially mobile", "Immobile"))
vital_signs = st.radio("Vital Signs Stability", ("Stable", "Unstable"))

# Rule-based model for discharge classification
def classify_discharge(age, length_of_stay, comorbidities, mobility, vital_signs):
    if length_of_stay <= 3 and comorbidities <= 1 and mobility == "Fully mobile" and vital_signs == "Stable":
        return "Will discharge today"
    else:
        return "Will not discharge today"

# Classify and display result
discharge_classification = classify_discharge(age, length_of_stay, comorbidities, mobility, vital_signs)
st.subheader(f"Discharge Classification: {discharge_classification}")
