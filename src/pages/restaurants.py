import streamlit as st
from backend import server
from state import state

def new():
    res_list = server.get_all_restaurants()
    
    # --- PRECISION HERO SECTION ---
    st.markdown(f"""
    <div style="
        background-image: linear-gradient(rgba(0,0,0,0.0), rgba(0,0,0,0.6)), url('https://picsum.photos/1400/600?random=1');
        background-size: cover;
        height: 480px;
        border-radius: 40px;
        padding: 80px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        border: 1px solid rgba(255,255,255,0.08);
        margin: 0 2%;
        box-shadow: 0 30px 60px rgba(0,0,0,0.5);
    ">
        <p style="text-transform: uppercase; letter-spacing: 6px; font-size: 0.7rem; margin-bottom: 5px; color: rgba(255,255,255,0.8); font-weight: 300;">Featured Experience</p>
        <h1 style="font-family: 'Playfair Display', serif; font-size: 6.5rem; margin: 0; color: white; line-height: 0.85; font-weight: 700;">Coast <span style="font-style: italic; opacity: 0.8;">&</span> Canopy</h1>
        <p style="font-size: 1.2rem; color: rgba(255,255,255,0.6); max-width: 450px; font-weight: 300; margin-top: 20px;">
            A culinary journey through forest and sea. By Chef Elena Rossi.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br><br>", unsafe_allow_html=True)
    
    # --- TRUE GOURMET RESTAURANT GRID ---
    # We use a custom flex container for better spacing control
    cols = st.columns(3, gap="large")
    for i, res in enumerate(res_list):
        col_idx = i % 3
        with cols[col_idx]:
            # The Card Visual Component (Literal clone of reference)
            st.markdown(f"""
            <div style="
                background: rgba(241, 245, 241, 0.08);
                backdrop-filter: blur(30px);
                border-radius: 45px;
                padding: 30px 25px;
                border: 1px solid rgba(255,255,255,0.08);
                margin-bottom: 25px;
                display: flex;
                align-items: center;
                gap: 25px;
                height: 180px;
            ">
                <img src="https://picsum.photos/140/140?random={res.restaurant_id}" style="border-radius: 50%; width: 110px; height: 110px; object-fit: cover; box-shadow: 0 15px 30px rgba(0,0,0,0.4); border: 2px solid rgba(255,255,255,0.1);">
                <div style="flex-grow: 1;">
                    <h4 style="margin: 0; font-family: 'Playfair Display', serif; font-size: 1.5rem; color: #ffffff;">{res.name}</h4>
                    <p style="margin: 3px 0 0 0; font-size: 0.75rem; color: rgba(255,255,255,0.4); font-weight: 300; line-height: 1.4;">Slow-cooked<br>Mediterranean cuisine</p>
                    <p style="margin-top: 10px; font-size: 0.65rem; color: rgba(255,255,255,0.5); letter-spacing: 1px;">Current Mood: <span style="color: #ffffff; font-weight: 500;">Calm</span></p>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 15px;">
                        <span style="text-decoration: underline; font-size: 0.8rem; letter-spacing: 1px; color: #ffffff; cursor: pointer;">Go to Menu</span>
                        <span style="color: #00E676; font-size: 0.65rem; letter-spacing: 2px;">★★★★★</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Action Trigger (Transparent Overlay)
            if st.button(f"SELECT_{res.restaurant_id}", key=f"res_btn_{res.restaurant_id}", width="stretch"):
                st.session_state.current_restaurant = res.restaurant_id
                st.session_state.page = "Menu"
                st.rerun()

    # Style the invisible buttons to occupy the card space
    st.markdown("""
    <style>
        div[data-testid="stColumn"] .stButton>button {
            margin-top: -205px !important;
            height: 180px !important;
            background: transparent !important;
            border: none !important;
            color: transparent !important;
        }
    </style>
    """, unsafe_allow_html=True)
