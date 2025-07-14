import streamlit as st
import requests
import os

st.set_page_config(page_title="AI 3D Model Generator", layout="centered")

st.title("🎨 AI → 3D Printable Model")

prompt = st.text_input("Describe your 3D object (e.g., 'A phone stand shaped like a cat')")

if st.button("Generate Model"):
    res = requests.post("http://n8n:5678/webhook/3d-model", json={"prompt": prompt})
    if res.status_code == 200:
        st.success("✅ Model generation started!")
    else:
        st.error("❌ Failed to submit. Try again.")

st.markdown("---")

preview_path = "output/preview.png"
stl_path = "output/result.stl"

# Show preview image if it exists
if os.path.exists(preview_path):
    st.image(preview_path, caption="🖼️ Preview Image", use_column_width=True)

# Show download button for STL
if os.path.exists(stl_path):
    with open(stl_path, "rb") as f:
        st.download_button(
            label="⬇️ Download STL",
            data=f,
            file_name="generated_model.stl",
