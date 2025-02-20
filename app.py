import pickle
import streamlit as st

st.set_page_config(page_title="Diabetes Classifier", page_icon="🌺", layout="centered")

# Load the model
diabetes_model_path = r"C:\Users\pavan\OneDrive\Desktop\Project\diabetes_model.sav"
diabetes_model = pickle.load(open(diabetes_model_path, 'rb'))

st.title("Diabetes Prediction using Machine Learning")

# Input fields
col1, col2, col3 = st.columns(3)
with col1:
    pregnancies = st.number_input("Pregnancies")
with col2:
    glucose = st.number_input("Glucose")
with col3:
    blood_pressure = st.number_input("Blood Pressure")
with col1:
    skin_thickness = st.number_input("Skin Thickness")
with col2:
    insulin = st.number_input("Insulin")
with col3:
    bmi = st.number_input("BMI")
with col1:
    diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function")
with col2:
    age = st.number_input("Age")

# Prediction button
if st.button("Predict"):
    # Gather the input data
    input_data = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]]
    
    # Make the prediction
    prediction = diabetes_model.predict(input_data)
    
    # Show result based on prediction
    if prediction[0] == 1:
        st.error("You have Diabetes")
    else:
        st.success("You don't have Diabetes")
with col1:
    accuracy = st.button("Check Accuracy")
    if accuracy:
        st.info("The accuracy of the model is 78.57%")
