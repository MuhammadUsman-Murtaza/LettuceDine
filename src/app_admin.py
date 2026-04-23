import streamlit as st
import os
import ssl
from state import state
from backend import server
from pages import admin

# --- SSL Fix ---
if not os.environ.get("PYTHONHTTPSVERIFY", ""):
    ssl._create_default_https_context = ssl._create_unverified_context

# --- Page Config ---
st.set_page_config(page_title="LettuceDine | Admin Console", page_icon="🛡️", layout="wide")

# --- Initialize State ---
state.initialize()
st.session_state.role = "Admin"

# --- GLOBAL OVERSIGHT UI CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,700&family=Inter:wght@300;400;500;900&display=swap');
    
    .block-container { padding-top: 1rem !important; }
    header {visibility: hidden; display: none;}
    footer {visibility: hidden;}
    
    .stApp {
        background: radial-gradient(circle at bottom right, #3D4F3F 0%, #0A0A0A 100%);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }

    /* Admin Sidebar Customization */
    [data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.03) !important;
        backdrop-filter: blur(40px);
        border-right: 1px solid rgba(255, 255, 255, 0.05);
        padding: 40px 10px;
    }

    /* Top Admin Bar */
    .admin-header {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        margin: 10px 1% 30px 1%;
        padding: 12px 30px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .admin-brand {
        display: flex;
        align-items: center;
        gap: 15px;
        font-family: 'Playfair Display', serif;
        font-size: 1.6rem;
    }
    
    .admin-profile {
        width: 35px;
        height: 35px;
        border-radius: 50%;
        background: url('https://picsum.photos/40/40?random=99');
        border: 2px solid #00E676;
    }
</style>
""", unsafe_allow_html=True)

# --- Top Header ---
st.markdown("""
<div class="admin-header">
    <div class="admin-brand">
        <span style="color: #00E676;">🥗</span> LettuceDine
    </div>
    <div class="admin-profile"></div>
</div>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("📊 Dashboard", width="stretch"): st.session_state.page = "Dashboard"; st.rerun()
    if st.button("🏪 Vendors", width="stretch"): st.session_state.page = "Vendors"; st.rerun()
    if st.button("🚚 Logistics", width="stretch"): st.session_state.page = "Logistics"; st.rerun()
    if st.button("💹 Analytics", width="stretch"): st.session_state.page = "Analytics"; st.rerun()
    if st.button("💰 Financials", width="stretch"): st.session_state.page = "Financials"; st.rerun()

# --- Content ---
admin.new()
