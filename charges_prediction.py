import streamlit as st
import numpy as np
import joblib

model=joblib.load('linear_regression_model.joblib')

#####
# Inject background color using HTML and CSS
st.markdown("""<style>.main {background-color: #f0f8ff; padding: 20px; border-radius: 10px; } </style> """, unsafe_allow_html=True)

# Wrap your content in a <div class="main">
st.markdown('<div class="main">', unsafe_allow_html=True)



#########




#st.title("********   RS Insurance   ******** ")
st.markdown("<h1 style='text-align: center; color: blue;'>********   RS Insurance   ********</h1>", unsafe_allow_html=True)


#st.header("   Insurance Charges Prediction   ")

st.markdown("<h2 style='text-align: center;'>Insurance Charges Prediction</h2>", unsafe_allow_html=True)

st.subheader("Enter the details to predict the insurance charges")

claim_amount=st.number_input("**Enter the claim amount:**",min_value=0.0,format="%.2f")
past_consultations=st.number_input("**Enter the number of past consultations:** ",min_value=0)
hospital_expenditure=st.number_input("**Enter the hospital expenditure:** ",min_value=0.0,format="%.2f")
annual_salary=st.number_input("**Enter the annual salary:** ",min_value=0.0,format="%.2f")
children=st.number_input("**Enter the number of children:** ",min_value=0)
smoker=st.selectbox("**Select the smoker status:** ",["Yes","No"])
smoker_encoded=1 if smoker=="Yes" else 0

# Close the div
st.markdown('</div>', unsafe_allow_html=True)

if st.button("**Predict Charges**"):
  input_data=np.array([[claim_amount,past_consultations,hospital_expenditure,annual_salary,children,smoker_encoded]])
  prediction=model.predict(input_data)[0]
  st.success(f"The predicted insurance charges are: ${prediction:.2f}")
