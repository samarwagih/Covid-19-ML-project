import streamlit as st
# import pickle
# import pandas as pd
# import sklearn



# Load the trained machine learning model
# model=pickle.load(open(r'.\Covid19.sav','rb'))


st.title("Covid-19 App")
# st.info('Application for Covid-19 Disease')

# st.sidebar.header('Feature Selection')

# USMER=st.text_input('USMER')
# MEDICAL_UNIT=st.text_input('MEDICAL_UNIT')
# SEX=st.text_input('SEX')
# PATIENT_TYPE=st.text_input('PATIENT_TYPE')
# PNEUMONIA=st.text_input('PNEUMONIA')
# AGE=st.text_input('AGE')
# PREGNANT=st.text_input('PREGNANT')
# DIABETES=st.text_input('DIABETES')
# COPD=st.text_input('COPD')
# ASTHMA=st.text_input('ASTHMA')
# INMSUPR=st.text_input('INMSUPR')
# HIPERTENSION=st.text_input('HIPERTENSION')
# OTHER_DISEASE=st.text_input('OTHER_DISEASE')
# CARDIOVASCULAR=st.text_input('CARDIOVASCULAR')
# OBESITY=st.text_input('OBESITY')
# RENAL_CHRONIC=st.text_input('RENAL_CHRONIC')
# TOBACCO=st.text_input('TOBACCO')
# DEATH=st.text_input('DEATH')
# PNEUMONIAe=st.text_input('PNEUMONIAe')
# Covid_or_Not=st.text_input('Covid_or_Not')
# NewAgeGroup_Children=st.text_input('NewAgeGroup_Children')
# NewAgeGroup_Middle_Aged_Adults=st.text_input('NewAgeGroup_Middle_Aged_Adults')
# NewAgeGroup_Seniors=st.text_input('NewAgeGroup_Seniors')
# NewAgeGroup_Young_Adults=st.text_input('NewAgeGroup_Young Adults ')

# df = pd.DataFrame({
#     'USMER': [USMER],
#     'MEDICAL_UNIT': [MEDICAL_UNIT],
#     'SEX': [SEX],
#     'PATIENT_TYPE': [PATIENT_TYPE],
#     'PNEUMONIA': [PNEUMONIA],
#     'AGE': [AGE],
#     'PREGNANT': [PREGNANT],
#     'DIABETES': [DIABETES],
#     'COPD': [COPD],
#     'ASTHMA': [ASTHMA],
#     'INMSUPR': [INMSUPR],
#     'HIPERTENSION': [HIPERTENSION],
#     'OTHER_DISEASE': [OTHER_DISEASE],
#     'CARDIOVASCULAR': [CARDIOVASCULAR],
#     'OBESITY': [OBESITY],
#     'RENAL_CHRONIC': [RENAL_CHRONIC],
#     'TOBACCO': [TOBACCO],
#     'DEATH': [DEATH],  
#     'PNEUMONIAe': [PNEUMONIAe],  
#     'Covid_or_Not': [Covid_or_Not],
#     'NewAgeGroup_Children': [NewAgeGroup_Children],
#     'NewAgeGroup_Middle_Aged_Adults': [NewAgeGroup_Middle_Aged_Adults],
#     'NewAgeGroup_Seniors': [NewAgeGroup_Seniors],
#     'NewAgeGroup_Young_Adults': [NewAgeGroup_Young_Adults]
# },index=[0])

# Con=st.sidebar.button('confirm')

# if Con:
#     result=model.predict(df)
#     st.write(result)