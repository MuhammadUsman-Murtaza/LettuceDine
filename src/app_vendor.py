import streamlit as st
import os
import ssl
from state import state
from backend import server
from pages import vendor

# --- SSL Fix ---
if not os.environ.get("PYTHONHTTPSVERIFY", ""):
    ssl._create_default_https_context = ssl._create_unverified_context

# --- Page Config ---
st.set_page_config(page_title="LettuceDine | Vendor Kitchen", page_icon="🥘", layout="wide")

# --- Initialize State ---
state.initialize()
st.session_state.role = "Vendor"

# --- ARTISANAL KITCHEN UI CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,700&family=Inter:wght@300;400;500;900&display=swap');
    
    .block-container { padding-top: 1.5rem !important; }
    header {visibility: hidden; display: none;}
    footer {visibility: hidden;}
    
    .stApp {
        background: radial-gradient(circle at top right, #3D4F3F 0%, #0A0A0A 100%);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }

    /* Production Central Header */
    .header-bar-central {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 25px;
        margin: 0px 2% 40px 2%;
        padding: 15px 50px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: relative;
    }
    
    .logo-mid {
        font-family: 'Playfair Display', serif;
        font-size: 2.2rem;
        font-weight: 700;
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
    }
    
    .nav-links-kitchen {
        display: flex;
        gap: 30px;
    }
    
    .kitchen-nav-item {
        font-size: 0.7rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: rgba(255,255,255,0.5);
    }
    
    .kitchen-nav-active {
        color: #ffffff;
        border-bottom: 2px solid #00E676;
        padding-bottom: 5px;
    }

    /* Secret Triggers */
    .stButton>button {
        background: transparent !important;
        border: none !important;
        color: transparent !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Header Layer ---
st.markdown(f"""
<div class="header-bar-central">
    <div class="nav-links-kitchen">
        <div class="kitchen-nav-item kitchen-nav-active">Kitchen</div>
        <div class="kitchen-nav-item">Curation</div>
        <div class="kitchen-nav-item">Analytics</div>
        <div class="kitchen-nav-item">Story</div>
    </div>
    <div class="logo-mid">LD</div>
    <div style="font-size: 0.7rem; letter-spacing: 2px; text-transform: uppercase; color: rgba(255,255,255,0.5);">Profile</div>
</div>
""", unsafe_allow_html=True)

# Invisible nav triggers (Simplified)
c1, c2, c3, c4, c5 = st.columns([1,1,1,1,6])
with c1: st.button("K", key="v_k")
with c2: st.button("C", key="v_c")
with c3: st.button("A", key="v_a")
with c4: st.button("S", key="v_s")

# --- Content ---
vendor.new()
