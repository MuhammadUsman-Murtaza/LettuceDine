import streamlit as st
from backend import server
from state import state

def new():
    customer = server.get_customer_profile(state.customer_id)
    
    # Account Header
    with st.container(border=True):
        c1, c2 = st.columns([1, 4], vertical_alignment="center")
        with c1:
            st.markdown("<h1 style='text-align:center; margin:0;'>👤</h1>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"## {customer.name if customer else 'Authenticated User'}")
            st.caption(f"Member since {customer.name[0] if customer else '?'}")
            st.markdown(f"📧 `{customer.email}` | 📞 `{customer.phone_num}`")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Logistic Centers Section
    st.markdown("### 📍 LOGISTIC CENTERS")
    addrs = server.get_customer_addresses(state.customer_id)
    
    grid = st.columns(2)
    for i, a in enumerate(addrs):
        with grid[i % 2]:
            with st.container(border=True):
                st.markdown(f"**{a.label.upper()}**")
                st.write(f"{a.street}")
                st.write(f"{a.city}")
                st.caption("Primary Delivery Point")

    st.markdown("---")
    
    # Add Hub
    with st.expander("➕ REGISTER NEW LOGISTIC HUB"):
        c_in1, c_in2 = st.columns(2)
        with c_in1:
            street = st.text_input("Street / Building")
            label = st.selectbox("Type", ["Home", "Work", "Partner", "Other"])
        with c_in2:
            city = st.text_input("Region / City")
            
        if st.button("Authorize Location", width="stretch"):
            if street and city:
                server.add_address(state.customer_id, street, city, "00000", label)
                st.toast("Location Authorized!", icon="📍")
                st.rerun()
            else:
                st.error("Validation failed: Empty fields detected.")
