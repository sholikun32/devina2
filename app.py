import streamlit as st
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="AI Avatar Chatbot", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    html, body, [class*="css"] {
        margin: 0;
        padding: 0;
        height: 100%;
        width: 100%;
        font-family: sans-serif;
        background: url('static/background.gif') no-repeat center center fixed;
        background-size: cover;
    }
    #response {
        color: white;
        background: rgba(0,0,0,0.6);
        padding: 10px 20px;
        border-radius: 8px;
        max-width: 90%;
        text-align: center;
        margin: 20px auto;
    }
    button {
        padding: 10px 20px;
        border: none;
        border-radius: 8px;
        background: #4caf50;
        color: white;
        font-size: 16px;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("## AI Avatar Chatbot")

# Render model-viewer via HTML
components.html(f"""
    <model-viewer 
      src="models/68819d08029c7e4cad137aea.glb"
      alt="AI Avatar"
      auto-rotate
      camera-controls
      shadow-intensity="1"
      style="width: 100%; height: 500px;">
    </model-viewer>
    <script type="module" src="https://unpkg.com/@google/model-viewer@4.1.0/dist/model-viewer.min.js"></script>
""", height=500)

# Show response text
if "response_text" not in st.session_state:
    st.session_state.response_text = "Halo! saya DEVINA. Ada yang bisa saya bantu? Tanya apa saja Boleeh!"

st.markdown(f"<div id='response'>{st.session_state.response_text}</div>", unsafe_allow_html=True)

# Simulate mic button
if st.button("🎤 Klik Untuk Bicara"):
    # Simulasi kirim suara → chatbot
    st.session_state.response_text = "Halo! saya adalah DEVINA Avatar Layanan Dinas Kesehatan Kota Semarang. Apa yang bisa saya bantu?"

# Refresh response
st.markdown(f"<div id='response'>{st.session_state.response_text}</div>", unsafe_allow_html=True)

