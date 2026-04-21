import streamlit as st
from backend import server
from state import state

def new():
    orders = server.get_customer_orders(state.customer_id)
    
    if not orders:
        st.info("No historical logs found.")
        return

    st.markdown("### 📋 TRANSACTION LOGS")

    def get_status_color(status):
        s = str(status).lower()
        if "delivered" in s: return "success"
        if "pending" in s: return "warning"
        return "error"

    for o in orders:
        with st.container(border=True):
            c1, c2, c3 = st.columns([2, 1, 1], vertical_alignment="center")
            status_text = str(o.status).split('.')[-1].upper()
            
            with c1:
                st.markdown(f"**ORDER #{o.order_id}**")
                st.caption(o.order_date.strftime('%d %B %Y | %H:%M'))
            with c2:
                st.write(f"**${o.total_amount:.2f}**")
            with c3:
                st.status(status_text, state=get_status_color(o.status))

            if "Delivered" in str(o.status):
                with st.expander("📝 Provide Feedback"):
                    rating = st.select_slider("Rating", options=[1,2,3,4,5], value=5, key=f"rate_{o.order_id}")
                    comment = st.text_area("Observations", placeholder="How was the food?", key=f"comm_{o.order_id}", label_visibility="collapsed")
                    if st.button("Publish Review", key=f"btn_{o.order_id}", width="stretch"):
                        server.submit_review(state.customer_id, o.restaurant_id, rating, comment)
                        st.toast("Review Published!", icon="🌟")
