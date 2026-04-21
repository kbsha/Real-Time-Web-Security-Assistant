import streamlit as st
import requests

st.title("AI Cyber Threat Detector")

text = st.text_input("Enter URL or message")

if st.button("Analyze"):

    response = requests.post(
        "https://ai-cyber-api.onrender.com/predict",
        json={"text": text}
    )

    result = response.json()

    st.success(result["prediction"])
    st.write("Confidence:", result["confidence"])