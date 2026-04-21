import streamlit as st

st.set_page_config(page_title="LettuceDine | Gateway", page_icon="🍱", layout="centered")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #050505; color: white; }
    .stButton>button {
        background: linear-gradient(135deg, #00E676 0%, #00C853 100%);
        color: black; border-radius: 12px; font-weight: 800; border: none; height: 3.5rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='color: #00E676; text-align: center; font-size: 3.5rem;'>LETTUCEDINE</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888; margin-top: -20px;'>MARKETPLACE CENTRAL SYSTEM</p>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.subheader("Select Your Access Portal")

with st.container(border=True):
    st.markdown("### 🍱 Customer Marketplace")
    st.write("Browse local vendors, purchase masterpieces, and track deliveries.")
    if st.button("Enter Marketplace", width="stretch"):
        st.info("In Production: You would now be redirected to https://market.lettucedine.com")
        st.caption("Local Test: Run 'streamlit run src/app_customer.py'")

st.markdown("<br>", unsafe_allow_html=True)

with st.container(border=True):
    st.markdown("### 🥘 Vendor Hub")
    st.write("Manage your restaurant operations, fulfillment, and menu inventory.")
    if st.button("Enter Vendor Portal", width="stretch", key="vend"):
        st.info("In Production: You would now be redirected to https://vendor.lettucedine.com")
        st.caption("Local Test: Run 'streamlit run src/app_vendor.py'")

st.markdown("<br>", unsafe_allow_html=True)

with st.container(border=True):
    st.markdown("### 🛡️ System Administration")
    st.write("Secure internal tools for marketplace oversight and global auditing.")
    if st.button("Enter Admin Command", width="stretch", key="admin"):
        st.info("In Production: Authorization Required.")
        st.caption("Local Test: Run 'streamlit run src/app_admin.py'")