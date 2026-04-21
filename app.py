import streamlit as st
from model import predict_text

st.set_page_config(page_title="AI Cyber Guard")

st.title("🛡️ AI Cyber Threat Detector")

text = st.text_input("Enter URL or message")

if st.button("Analyze"):

    result = predict_text(text)

    st.success(result["prediction"])
    st.write("Confidence:", result["confidence"], "%")