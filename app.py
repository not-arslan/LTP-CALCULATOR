```
import streamlit as st
import pandas as pd
from ltp_calculator import calculate_nifty_option_profit_loss

st.title("Nifty Options LTP Calculator with Option Chain")

# Mock option chain data (replace with NSE API for real-time data)
option_chain_data = {
    "Strike Price": [24500, 24600, 24700, 24800, 24900, 25000, 25100, 25200, 25300, 25400],
    "Call LTP": [250.5, 200.3, 150.7, 110.2, 80.5, 55.1, 35.2, 20.8, 12.3, 8.5],
    "Call OI": [50000, 45000, 40000, 35000, 30000, 25000, 20000, 15000, 10000, 5000],
    "Put LTP": [10.2, 15.4, 22.1, 30.5, 40.8, 55.3, 75.6, 100.2, 130.7, 165.4],
    "Put OI": [6000, 8000, 10000, 12000, 15000, 20000, 25000, 30000, 35000, 40000]
}
option_chain = pd.DataFrame(option_chain_data)

# Display option chain
st.subheader("Nifty Option Chain")
st.dataframe(option_chain, use_container_width=True)

# Calculator inputs
st.subheader("Profit/Loss Calculator")
option_type = st.selectbox("Option Type", ["Call", "Put"])
strike_price = st.number_input("Strike Price", min_value=0.0, step=100.0, value=25000.0)
spot_price = st.number_input("Current Nifty Spot Price", min_value=0.0, step=100.0, value=25200.0)
premium = st.number_input("Premium Paid per Unit", min_value=0.0, step=10.0, value=100.0)
lot_size = st.number_input("Lot Size (e.g., 25 for Nifty)", min_value=1, value=25, step=1)
num_lots = st.number_input("Number of Lots", min_value=1, value=1, step=1)

if st.button("Calculate"):
    result = calculate_nifty_option_profit_loss(option_type.lower(), strike_price, spot_price, premium, lot_size, num_lots)
    if "error" in result:
        st.error(result["error"])
    else:
        st.success(f"**Profit/Loss**: ₹{result['profit_loss']}")
        st.info(f"**Break-Even Point**: ₹{result['break_even']}")
        st.info(f"**Total Premium Paid**: ₹{result['total_premium_paid']}")
        st.warning(f"**OI Insight**: {result['oi_insight']}")
```
