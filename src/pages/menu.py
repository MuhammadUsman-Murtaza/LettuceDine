import streamlit as st
from backend import server
from state import state

def new():
    res_id = st.session_state.current_restaurant
    if not res_id:
        st.session_state.page = "Explore"
        st.rerun()
        
    menu_items = server.get_menu_for_restaurant(res_id)
    
    # Navigation Hub
    st.markdown("""
    <div style="display: flex; gap: 10px; align-items: center; margin-bottom: 2rem;">
        <span style="font-size: 0.7rem; letter-spacing: 2px; color: rgba(255,255,255,0.4);">RESTAURANT SELECTION</span>
        <span style="color: rgba(255,255,255,0.2);">/</span>
        <span style="font-size: 0.7rem; letter-spacing: 2px; color: #00E676;">DISH CATALOG</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2 style='font-family: \"Playfair Display\", serif; font-size: 3rem;'>Our Signature Curation</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Dish List in Gourmet Glass Cards
    for item in menu_items:
        with st.container():
            st.markdown(f"""
            <div style="
                background: rgba(241, 245, 241, 0.05);
                backdrop-filter: blur(25px);
                border-radius: 40px;
                padding: 30px;
                border: 1px solid rgba(255,255,255,0.05);
                margin-bottom: 20px;
                display: flex;
                align-items: center;
                gap: 30px;
            ">
                <img src="https://picsum.photos/150/150?random={item.item_id+100}" style="border-radius: 50%; width: 120px; height: 120px; object-fit: cover; border: 3px solid rgba(255,255,255,0.1);">
                <div style="flex-grow: 1;">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                        <h3 style="margin: 0; font-family: 'Playfair Display', serif; font-size: 2rem; color: #ffffff;">{item.name}</h3>
                        <span style="font-family: 'Playfair Display', serif; font-size: 1.8rem; color: #00E676; font-style: italic;">${item.price:.2f}</span>
                    </div>
                    <p style="margin-top: 10px; font-size: 0.95rem; color: rgba(255,255,255,0.6); max-width: 600px; font-weight: 300;">
                        {item.description if item.description else "An artisanal blend of seasonal ingredients, masterfully prepared by our resident chefs."}
                    </p>
                    <p style="margin-top: 15px; font-size: 0.7rem; color: #00E676; letter-spacing: 1px;">PREMIUM SELECTION</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Discreet 'Plus' button for adding to cart
            if st.button(f"Add {item.name}", key=f"add_{item.item_id}", width="stretch"):
                state.add_to_cart(item)
                st.toast(f"Selection Captured: {item.name}", icon="✨")
