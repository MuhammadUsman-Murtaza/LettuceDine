import streamlit as st
import pandas as pd
import altair as alt
from backend import server
from state import state

def new():
    # Context: For the demo, we assume we are managing the first restaurant
    res_list = server.get_all_restaurants()
    vendor_id = 1 # Coast & Canopy (Demo)
    vendor_name = "Chef Elena"
    
    current_res = res_list[0] if res_list else None
    
    # 1. GREETING
    st.markdown(f"<h1 style='font-family: \"Playfair Display\", serif; font-size: 3.5rem; margin-bottom: 2rem;'>Peaceful Evening, {vendor_name}</h1>", unsafe_allow_html=True)
    
    c_main, c_side = st.columns([2.5, 1], gap="large")
    
    with c_main:
        # 2. KITCHEN FLOW CHART
        st.markdown("<p style='letter-spacing: 2px; font-size: 0.9rem; margin-bottom: 1rem;'>Kitchen Flow</p>", unsafe_allow_html=True)
        
        # Generating aesthetic mock data for the 'Flow'
        chart_data = pd.DataFrame({
            'Time': ["00am", "3am", "6am", "10am", "12pm", "15pm", "10pm"] * 2,
            'Volume': [50, 80, 150, 320, 280, 380, 200, 30, 60, 120, 200, 250, 420, 150],
            'Series': ['Kitchen A'] * 7 + ['Kitchen B'] * 7
        })
        
        flow_chart = alt.Chart(chart_data).mark_area(
            interpolate='basis',
            fillOpacity=0.3,
            line={'color': '#00E676', 'width': 3}
        ).encode(
            x=alt.X('Time:O', sort=None, axis=alt.Axis(labelAngle=0, labelColor='rgba(255,255,255,0.4)')),
            y=alt.Y('Volume:Q', axis=None),
            color=alt.Color('Series:N', scale=alt.Scale(range=['#00E676', '#FFD700']), legend=None)
        ).properties(height=300).configure_view(strokeOpacity=0)
        
        st.altair_chart(flow_chart, use_container_width=True)

        # 3. ACTIVE EXPERIENCES
        st.markdown("<br><p style='letter-spacing: 2px; font-size: 0.9rem; margin-top: 2rem;'>Active Experiences</p>", unsafe_allow_html=True)
        
        active_orders = server.get_customer_orders(1) # Using orders for restaurant 1
        for o in active_orders[:3]:
             st.markdown(f"""
            <div style="
                background: rgba(255, 255, 255, 0.03);
                border-radius: 20px;
                padding: 20px 30px;
                border: 1px solid rgba(255, 255, 255, 0.05);
                margin-bottom: 10px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            ">
                <span style="font-size: 0.9rem; color: rgba(255,255,255,0.8);"><b>{current_res.name if current_res else 'Experience'}</b>: Session #{o.order_id} • Preparing</span>
                <div style="background: rgba(0, 230, 118, 0.1); border: 1px solid #00E676; padding: 4px 15px; border-radius: 12px; font-size: 0.7rem; color: #00E676; box-shadow: 0 0 10px rgba(0, 230, 118, 0.2);">● Preparing</div>
            </div>
            """, unsafe_allow_html=True)

    with c_side:
        # 4. SIDEBAR METRICS
        # Daily Nectar
        with st.container(border=True):
            st.markdown(f"""
                <p style="font-size: 0.8rem; color: rgba(255,255,255,0.5); margin:0;">Daily Nectar</p>
                <h2 style="margin:0; font-family: 'Inter', sans-serif; font-weight: 400; font-size: 2.5rem;">$1,250</h2>
                <p style="font-size: 0.7rem; color: #00E676;">Earnings Today</p>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Guest Gratitude
        with st.container(border=True):
            avg_rating = float(current_res.rating) if current_res else 4.9
            st.markdown(f"""
                <p style="font-size: 0.8rem; color: rgba(255,255,255,0.5); margin:0;">Guest Gratitude</p>
                <h2 style="margin:0; font-family: 'Inter', sans-serif; font-weight: 400; font-size: 2.5rem;">{avg_rating} <span style="color: #FFD700; font-size: 1.5rem;">★</span></h2>
                <p style="font-size: 0.75rem; color: rgba(255,255,255,0.6); font-style: italic; margin-top: 10px;">
                    "How we are honorious. Chef Elena"
                </p>
            """, unsafe_allow_html=True)
