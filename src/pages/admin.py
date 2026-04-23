import streamlit as st
import pandas as pd
import altair as alt
from backend import server
from state import state

def new():
    # Fetching real system stats
    res_list = server.get_all_restaurants()
    orders = server.get_customer_orders(None) # Fetch all global orders
    total_rev = sum(o.total_amount for o in orders)
    active_count = sum(1 for o in orders if "Delivered" not in str(o.status))

    # --- TOP INTELLIGENCE ROW ---
    c_rev, c_ord, c_app = st.columns(3, gap="medium")
    
    with c_rev:
        # Sparkline Data
        spark_data = pd.DataFrame({'x': range(10), 'y': [2, 3, 2, 4, 3, 5, 4, 6, 5, 8]})
        spark = alt.Chart(spark_data).mark_line(
            interpolate='monotone', stroke='#FFD700', strokeWidth=3
        ).encode(x=alt.X('x', axis=None), y=alt.Y('y', axis=None)).properties(height=60)

        with st.container(border=True):
            st.markdown(f"<p style='font-size: 0.8rem; color: rgba(255,255,255,0.5); margin:0;'>Total Revenue</p>", unsafe_allow_html=True)
            st.markdown(f"<h1 style='margin:0; font-size: 2.5rem;'>${total_rev:,.0f}</h1>", unsafe_allow_html=True)
            st.altair_chart(spark, use_container_width=True)

    with c_ord:
        with st.container(border=True):
            st.markdown(f"<p style='font-size: 0.8rem; color: rgba(255,255,255,0.5); margin:0;'>Active Orders</p>", unsafe_allow_html=True)
            st.markdown(f"<h1 style='margin:0; font-size: 2.5rem; color: #00E676;'>{active_count}</h1>", unsafe_allow_html=True)
            st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

    with c_app:
        with st.container(border=True):
            st.markdown(f"<p style='font-size: 0.8rem; color: rgba(255,255,255,0.5); margin:0;'>Vendor Applications</p>", unsafe_allow_html=True)
            st.markdown(f"<h1 style='margin:0; font-size: 2.5rem; color: #BD10E0;'>73</h1>", unsafe_allow_html=True)
            st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- MAIN OVERSIGHT ROW ---
    c_map, c_feed = st.columns([2, 1], gap="large")
    
    with c_map:
        st.markdown("<p style='letter-spacing: 2px; font-size: 0.8rem;'>Live Marketplace Map</p>", unsafe_allow_html=True)
        # Emulating the 'Glow' map with a dark-themed area
        st.markdown(f"""
        <div style="
            background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.8)), url('https://picsum.photos/800/500?random=15');
            background-size: cover;
            height: 400px;
            border-radius: 30px;
            border: 1px solid rgba(255,255,255,0.05);
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
        ">
            <span style="color: #00E676; font-size: 0.7rem; letter-spacing: 2px;">LOGISTICS INTERFACE ACTIVE</span>
            <div style="position: absolute; top: 100px; left: 200px; width: 10px; height: 10px; background: #00E676; border-radius: 50%; box-shadow: 0 0 20px #00E676;"></div>
            <div style="position: absolute; bottom: 150px; right: 180px; width: 10px; height: 10px; background: #FFD700; border-radius: 50%; box-shadow: 0 0 20px #FFD700;"></div>
        </div>
        """, unsafe_allow_html=True)

    with c_feed:
        st.markdown("<p style='letter-spacing: 2px; font-size: 0.8rem;'>Recent Activity</p>", unsafe_allow_html=True)
        for i in range(3):
            with st.container(border=True):
                st.markdown(f"""
                <div style="display: flex; gap: 15px; align-items: start;">
                    <img src="https://picsum.photos/40/40?random={i+10}" style="border-radius: 50%; width: 35px; height: 35px;">
                    <div>
                        <p style="margin:0; font-size: 0.85rem; font-weight: 700;">New vendor</p>
                        <p style="margin:0; font-size: 0.7rem; color: rgba(255,255,255,0.4);">Updated 12h ago</p>
                        <div style="display: flex; gap: 5px; margin-top: 5px;">
                            <img src="https://picsum.photos/50/40?random={i+20}" style="border-radius: 5px; width: 40px;">
                            <img src="https://picsum.photos/50/40?random={i+30}" style="border-radius: 5px; width: 40px;">
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
