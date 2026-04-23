import streamlit as st
from backend import server
from state import state
import time

def new():
    if not st.session_state.cart:
        st.markdown("<div style='text-align:center; padding: 100px;'>", unsafe_allow_html=True)
        st.markdown("<h2 style='font-family: \"Playfair Display\", serif; opacity: 0.3;'>Your Basket is a Blank Canvas</h2>", unsafe_allow_html=True)
        if st.button("RETURN TO MARKETPLACE", width="stretch"):
            st.session_state.page = "Explore"
            st.rerun()
        return

    st.markdown("<h2 style='font-family: \"Playfair Display\", serif; font-size: 3rem;'>Transaction Summary</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    col_input, col_summary = st.columns([1.5, 1], gap="large")
    
    with col_input:
        st.markdown("### 1. LOGISTICS")
        with st.container(border=True):
            addrs = server.get_customer_addresses(state.customer_id)
            if not addrs:
                st.error("No Delivery Points Identified.")
                if st.button("ESTABLISH LOCATION"):
                    st.session_state.page = "Profile"
                    st.rerun()
                return
                
            addr_options = {f"{a.label}: {a.street}": a.address_id for a in addrs}
            selected_label = st.selectbox("Destination Hub", options=list(addr_options.keys()))
            state.selected_address = addr_options[selected_label]

    with col_summary:
        st.markdown("### 2. STATEMENT")
        with st.container():
            st.markdown(f"""
            <div style="
                background: rgba(255,255,255,0.03); 
                padding: 30px; 
                border-radius: 30px; 
                border: 1px solid rgba(255,255,255,0.05);
            ">
                <p style="letter-spacing: 2px; font-size: 0.7rem; color: rgba(255,255,255,0.5);">SELECTION BREAKDOWN</p>
            """, unsafe_allow_html=True)
            
            subtotal = state.get_cart_total()
            delivery_fee = 2.50
            total = subtotal + delivery_fee
            
            for item_id, d in st.session_state.cart.items():
                st.write(f"{d['quantity']}x {d['item'].name} — ${d['item'].price * d['quantity']:.2f}")
            
            st.markdown(f"""
                <hr style="opacity: 0.1;">
                <div style="display: flex; justify-content: space-between;">
                    <span style='color: rgba(255,255,255,0.5);'>Subtotal</span>
                    <span>${subtotal:.2f}</span>
                </div>
                <div style="display: flex; justify-content: space-between; margin-top: 10px;">
                    <span style='color: rgba(255,255,255,0.5);'>Service Fee</span>
                    <span>$2.50</span>
                </div>
                <div style="display: flex; justify-content: space-between; margin-top: 20px;">
                    <span style='font-family: \"Playfair Display\", serif; font-size: 1.5rem;'>Total</span>
                    <span style='font-family: \"Playfair Display\", serif; font-size: 1.8rem; color: #00E676;'>${total:.2f}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("AUTHORIZE TRANSACTION", width="stretch"):
                with st.spinner("Processing High-Priority Order..."):
                    order_id = server.place_order(
                        customer_id=state.customer_id,
                        restaurant_id=st.session_state.current_restaurant,
                        address_id=state.selected_address,
                        cart_items=st.session_state.cart,
                        total_amount=total,
                        payment_method="Market Authorization"
                    )
                    state.clear_cart()
                    st.balloons()
                    st.success(f"Capture Confirmed: #{order_id}")
                    time.sleep(1.5)
                    st.session_state.page = "Orders"
                    st.rerun()
