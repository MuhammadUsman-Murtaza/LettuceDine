import streamlit as st
import os
import ssl
from state import state
from backend import server
from pages import restaurants, menu, checkout, profile, order_history

# --- SSL Fix ---
if not os.environ.get("PYTHONHTTPSVERIFY", ""):
    ssl._create_default_https_context = ssl._create_unverified_context

# --- Page Config ---
st.set_page_config(page_title="LettuceDine | Marketplace", page_icon="🍱", layout="wide")

# --- Initialize State ---
state.initialize()
st.session_state.role = "Customer"

# --- 100% PRODUCTION CSS - ZERO-GAP REFINEMENT ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,700&family=Inter:wght@300;400;500;900&display=swap');
    
    /* Force Remove Streamlit's Default Padding */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 0rem !important;
    }
    
    header {visibility: hidden; display: none;}
    footer {visibility: hidden;}
    
    .stApp {
        background: radial-gradient(circle at top left, #3D4F3F 0%, #0A0A0A 100%);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }

    /* Production Floating Header - Refined Spacing */
    .header-bar {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 25px;
        margin: 0px 2% 20px 2%; /* Reduced top margin to 0 */
        padding: 15px 40px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: relative;
        z-index: 1000;
    }
    
    .brand-full {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        font-weight: 700;
        letter-spacing: -1px;
        color: #ffffff;
    }
    
    .nav-links-row {
        display: flex;
        gap: 40px;
    }
    
    .nav-item {
        font-size: 0.75rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: rgba(255,255,255,0.6);
        cursor: pointer;
        position: relative;
    }
    
    .nav-active {
        color: #ffffff;
    }
    .nav-active::after {
        content: '';
        position: absolute;
        bottom: -8px;
        left: 0;
        width: 100%;
        height: 2px;
        background: #00E676;
    }

    /* Overlay invisibility logic */
    .stButton>button {
        background: transparent !important;
        border: none !important;
        color: transparent !important;
        height: 45px !important;
        margin-top: -65px !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Integrated Header View ---
current = st.session_state.page
st.markdown(f"""
<div class="header-bar">
    <div class="brand-full">LettuceDine</div>
    <div class="nav-links-row">
        <div class="nav-item {'nav-active' if current == 'Explore' else ''}">Explore</div>
        <div class="nav-item {'nav-active' if current == 'Orders' else ''}">Experiences</div>
        <div class="nav-item">Journal</div>
        <div class="nav-item {'nav-active' if current == 'Profile' else ''}">Profile</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Invisible triggers
c_nav_space, c_b1, c_b2, c_b3, c_b4 = st.columns([7, 1, 1, 1, 1.2])
with c_b1: 
    if st.button(" ", key="nav_exp"): st.session_state.page = "Explore"; st.rerun()
with c_b2: 
    if st.button(" ", key="nav_ord"): st.session_state.page = "Orders"; st.rerun()
with c_b4: 
    if st.button(" ", key="nav_prf"): st.session_state.page = "Profile"; st.rerun()

# --- Switcher ---
page = st.session_state.page
if page == "Explore": restaurants.new()
elif page == "Menu": menu.new()
elif page == "Checkout": checkout.new()
elif page == "Orders": order_history.new()
elif page == "Profile": profile.new()
