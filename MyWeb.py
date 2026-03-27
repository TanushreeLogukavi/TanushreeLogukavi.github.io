import streamlit as st
from nilearn import plotting, datasets
import streamlit.components.v1 as components

st.set_page_config(page_title="Brain Visualization", page_icon="🧠")

# Styling to match the Professional Pink/Times New Roman theme
st.markdown("""
    <style>
    .stApp { background-color: #fffafa; }
    h1, h2, h3 { color: #ad1457 !important; font-family: "Times New Roman", serif; }
    .stButton>button { background-color: #ad1457; color: white; border-radius: 20px; }
    p { font-family: "Times New Roman", serif; font-size: 1.1rem; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧠 Neuroimaging Visualization")
st.write("Interactive 3D Glass Brain visualization powered by Nilearn.")

# --- GLASS BRAIN SECTION ---
st.subheader("3D Glass Brain View")

# Using a standard MNI template for the glass brain
# In the future, you can replace this with your actual FTD patient data maps
with st.spinner("Generating 3D Brain View..."):
    # Create the glass brain plot (interactive)
    view = plotting.view_img(
        datasets.load_mni152_template(), 
        threshold=3, 
        bg_img=None, 
        opacity=0.2,
        title="Interactive Glass Brain"
    )
    
    # Render the interactive plot in Streamlit
    components.html(view.get_iframe(), height=500)

st.markdown("""
    <div style="background:#fff0f5; padding:15px; border-radius:10px; border:1px solid #f8bbd0;">
        <p><b>Note:</b> You can use your mouse to rotate, zoom, and click on different 
        coordinates to see the cross-sections of the MNI152 template.</p>
    </div>
""", unsafe_allow_html=True)

# Hidden Analytics Tracking
st.components.v1.html("""
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-CJJJWY9LRH"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-CJJJWY9LRH');
    </script>
    """, height=0)
