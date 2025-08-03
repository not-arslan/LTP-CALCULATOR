# app.py
import streamlit as st
from ltp_calculator import calculate_nifty_option_profit_loss

st.title("Nifty Options LTP Calculator")

# Input form
option_type = st.selectbox("Option Type", ["Call", "Put"])
strike_price = st.number_input("Strike Price", min_value=0.0, step=100.0)
spot_price = st.number_input("Current Nifty Spot Price", min_value=0.0, step=100.0)
premium = st.number_input("Premium Paid per Unit", min_value=0.0, step=10.0)
lot_size = st.number_input("Lot Size (e.g., 25 for Nifty)", min_value=1, value=25, step=1)
num_lots = st.number_input("Number of Lots", min_value=1, step=1)

if st.button("Calculate"):
    result = calculate_nifty_option_profit_loss(option_type.lower(), strike_price, spot_price, premium, lot_size, num_lots)
    if "error" in result:
        st.error(result["error"])
    else:
        st.success(f"**Profit/Loss**: ₹{result['profit_loss']}")
        st.info(f"**Break-Even Point**: ₹{result['break_even']}")
        st.info(f"**Total Premium Paid**: ₹{result['total_premium_paid']}")
        st.warning(f"**OI Insight**: {result['oi_insight']}")
