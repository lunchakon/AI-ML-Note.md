import streamlit as st
import requests

st.title("🧠 Prompt to 3D Model")
prompt = st.text_input("Enter 3D design idea:")

if st.button("Submit"):
    res = requests.post("http://n8n:5678/webhook/3d-model", json={"prompt": prompt})
    st.success("Submitted to workflow!")
