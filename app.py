import streamlit as st
import joblib

# st.title("Rayan")
# model = joblib.load("svc.pkl")

# st.write('##Loan Prediction')

# x = st.slider('experience', 0 , 40)
# # Predict accepts only 2 dimension
# # Do reshape or like the bottom line
# y = model.predict([[x]])

# st.write('Loan Condition is')

st.title("Rayan")
# model = joblib.load("svc.pkl")

st.write('BMI')

hieght = ((st.slider('Height', 1 , 200))/100)
wieght  = st.slider('Weight :', 1, 200)
bmi = wieght / (hieght * hieght)
st.write(bmi)
