# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:05:06 2025

@author: Divya
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 17:09:32 2025

@author: Divya
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


with open('diabetes_pred.sav', 'rb') as file:
    diabetes_model = pickle.load(file)

with open('heart_disease_pred.sav', 'rb') as file:
    heart_disease_model = pickle.load(file)

with open("parkinson's_disease_pred.sav", 'rb') as file:
    parkinsons_disease_model = pickle.load(file)

with st.sidebar:
    
    selected= option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Predtion',
         'Heart Disease Prediction',
         'Parkinsons Prediction'],
        
        icons=['activity','heart','person'],
        
         default_index=0
        )
    
if(selected=='Diabetes Predtion'):
    #page title
    st.title('Diabetes Prediction using ML')
    
    #columns for input
    col1, col2, col3= st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure of the Person")
    with col1:
        SkinThickness = st.text_input("Skin Thickness value")
    with col2:
        Insulin = st.text_input("Insulin")
    with col3:
        BMI = st.text_input("BMI value")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")
    with col2:
        Age = st.text_input("Age of the person")

# Placeholder for prediction
    diab_diagnosis = ''

    # Validate inputs
    if st.button('Diabetes Test Result'):
        if all([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]):
            try:
                # Convert inputs to numeric
                Pregnancies = int(Pregnancies)
                Glucose = float(Glucose)
                BloodPressure = float(BloodPressure)
                SkinThickness = float(SkinThickness)
                Insulin = float(Insulin)
                BMI = float(BMI)
                DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
                Age = int(Age)
                
                # Make prediction
                diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
                
                if diab_prediction[0] == 1:
                    st.markdown('<div style="background-color:red;padding:10px;border-radius:5px;color:white">The Person is Diabetic</div>', unsafe_allow_html=True)
                else:
                    st.success('The Person is NOT Diabetic')
            except ValueError:
                st.error("Please enter valid numeric values for all fields.")
        
# Heart Disease Prediction
if selected == 'Heart Disease Prediction':
    # Page title
    st.title('Heart Disease Prediction using ML')
    
    
    # Columns for input
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input("Sex (1 = Male, 0 = Female)")
    with col3:
        cp = st.text_input("Chest Pain Type (0, 1, 2, 3)")
    with col1:
        trestbps = st.text_input("Resting Blood Pressure (mm Hg)")
    with col2:
        chol = st.text_input("Cholesterol Level (mg/dl)")
    with col3:
        fbs = st.text_input("Fasting Blood Sugar (>120 mg/dl, 1 = True, 0 = False)")
    with col1:
        restecg = st.text_input("Resting Electrocardiographic Results (0, 1, 2)")
    with col2:
        thalach = st.text_input("Maximum Heart Rate Achieved")
    with col3:
        exang = st.text_input("Exercise-Induced Angina (1 = Yes, 0 = No)")
    with col1:
        oldpeak = st.text_input("ST Depression Induced by Exercise")
    with col2:
        slope = st.text_input("Slope of the Peak Exercise ST Segment (0, 1, 2)")
    with col3:
        ca = st.text_input("Number of Major Vessels (0-3) Colored by Fluoroscopy")
    with col1:
        thal = st.text_input("Thalassemia (0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect)")

    # Code for prediction
    heart_diagnosis = ''

    # Creating a button for prediction
    if st.button('Heart Disease Test Result'):
        # Check if all fields are filled before conversion
        if not all([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]):
            st.error("Please fill in all fields before submitting.")
        else:
            try:
                # Convert inputs to numeric values
                age = int(age)
                sex = int(sex)
                cp = int(cp)
                trestbps = float(trestbps)
                chol = float(chol)
                fbs = int(fbs)
                restecg = int(restecg)
                thalach = float(thalach)
                exang = int(exang)
                oldpeak = float(oldpeak)
                slope = int(slope)
                ca = int(ca)
                thal = int(thal)

                # Make prediction
                heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
                
                if heart_prediction[0] == 1:
                    st.markdown('<div style="background-color:red;padding:10px;border-radius:5px;color:white">The Person has Heart Disease</div>', unsafe_allow_html=True)
                else:
                    st.success('The Person does NOT have Heart Disease')
                
             
            except ValueError:
                st.error("Please enter valid numeric values for all fields.")


if selected == 'Parkinsons Prediction':
    # Page title
    st.title("Parkinson's Prediction using ML")
    
    # User Input with five columns
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        name = st.text_input("Name")
    with col2:
        MDVP_Fo_Hz = st.text_input("MDVP:Fo(Hz)")
    with col3:
        MDVP_Fhi_Hz = st.text_input("MDVP:Fhi(Hz)")
    with col4:
        MDVP_Flo_Hz = st.text_input("MDVP:Flo(Hz)")
    with col5:
        MDVP_Jitter_Percent = st.text_input("MDVP:Jitter(%)")

    with col1:
        MDVP_Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")
    with col2:
        MDVP_RAP = st.text_input("MDVP:RAP")
    with col3:
        MDVP_PPQ = st.text_input("MDVP:PPQ")
    with col4:
        Jitter_DDP = st.text_input("Jitter:DDP")
    with col5:
        MDVP_Shimmer = st.text_input("MDVP:Shimmer")

    with col1:
        MDVP_Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
    with col2:
        Shimmer_APQ3 = st.text_input("Shimmer:APQ3")
    with col3:
        Shimmer_APQ5 = st.text_input("Shimmer:APQ5")
    with col4:
        MDVP_APQ = st.text_input("MDVP:APQ")
    with col5:
        Shimmer_DDA = st.text_input("Shimmer:DDA")

    with col1:
        NHR = st.text_input("NHR")
    with col2:
        HNR = st.text_input("HNR")
    with col3:
        RPDE = st.text_input("RPDE")
    with col4:
        DFA = st.text_input("DFA")
    with col5:
        spread1 = st.text_input("Spread1")

    with col1:
        spread2 = st.text_input("Spread2")
    with col2:
        D2 = st.text_input("D2")
    with col3:
        PPE = st.text_input("PPE")
    
    # Placeholder for the result
    parkinsons_diagnosis = ''
    
    if st.button("Parkinson's Test Result"):
        try:
            # Convert all inputs to float before prediction
            inputs = [
                float(MDVP_Fo_Hz), float(MDVP_Fhi_Hz), float(MDVP_Flo_Hz), float(MDVP_Jitter_Percent),
                float(MDVP_Jitter_Abs), float(MDVP_RAP), float(MDVP_PPQ), float(Jitter_DDP),
                float(MDVP_Shimmer), float(MDVP_Shimmer_dB), float(Shimmer_APQ3), float(Shimmer_APQ5),
                float(MDVP_APQ), float(Shimmer_DDA), float(NHR), float(HNR), float(RPDE),
                float(DFA), float(spread1), float(spread2), float(D2), float(PPE)
            ]
            
            # Make prediction
            parkinsons_prediction = parkinsons_disease_model.predict([inputs])
            
            # Display result
            if parkinsons_prediction[0] == 1:
                st.success("The person has Parkinson's Disease.")
            else:
                st.success("The person does not have Parkinson's Disease.")
        
        except ValueError:
            st.error("Please enter valid numeric values in all fields.")
