import streamlit as st
import pickle


model, scaler = pickle.load(open('model.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))


st.title("Height Weight Prediction")
st.title("Enter Weight to get your Hieght")

Weight = st.slider("Select Weight", 0, 120)

if st.button("Predict"):
    scaled_input = scaler.transform([[Weight]])
    prediction = model.predict(scaled_input)
    st.title("Height predicted is "  + str(prediction[0]) )