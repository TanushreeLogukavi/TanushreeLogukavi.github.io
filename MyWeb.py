import streamlit as st
import numpy as np

st.set_page_config(page_title="Brain Age Tool", page_icon="🧠")

# Custom CSS for the Pink Theme
st.markdown("""
    <style>
    .stApp { background-color: #fffafa; }
    h1, h2 { color: #ad1457; font-family: "Times New Roman", serif; }
    .stButton>button { background-color: #ad1457; color: white; border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧠 Brain Age Calculator")
st.write("This is a computational demo for structural MRI analysis.")

# Simple Interactive Demo
age = st.number_input("Enter Chronological Age:", min_value=1, max_value=100, value=25)
brain_volume = st.slider("Total Gray Matter Volume (liters):", 0.5, 1.5, 1.1)

# Mock calculation for the demo
predicted_age = age + (1.2 - brain_volume) * 10 

if st.button("Calculate Predicted Brain Age"):
    st.success(f"Predicted Brain Age: **{predicted_age:.2f} years**")
    diff = predicted_age - age
    st.write(f"Brain Age Gap: {diff:+.2f} years")

st.info("Note: This is a demo interface. The underlying model is based on structural MRI preprocessing via fMRIPrep.")

# Hidden Analytics
st.components.v1.html("""
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-CJJJWY9LRH"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-CJJJWY9LRH');
    </script>
    """, height=0)
