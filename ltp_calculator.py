```
def calculate_nifty_option_profit_loss(option_type, strike_price, spot_price, premium, lot_size, num_lots):
    """
    Calculate profit or loss for a Nifty option trade.
    
    Parameters:
    - option_type (str): 'call' or 'put'
    - strike_price (float): Strike price of the option
    - spot_price (float): Current Nifty index price
    - premium (float): Premium paid per unit
    - lot_size (int): Number of units per lot (e.g., 25 for Nifty)
    - num_lots (int): Number of lots traded
    
    Returns:
    - dict: Contains profit/loss, break-even point, and basic insights
    """
    try:
        if option_type.lower() not in ['call', 'put']:
            return {"error": "Invalid option type. Use 'call' or 'put'."}
        if any(x < 0 for x in [strike_price, spot_price, premium, lot_size, num_lots]):
            return {"error": "Inputs cannot be negative."}
        
        total_units = lot_size * num_lots
        total_premium = premium * total_units
        
        if option_type.lower() == 'call':
            intrinsic_value = max(0, spot_price - strike_price)
            profit_loss = (intrinsic_value - premium) * total_units
            break_even = strike_price + premium
        else:
            intrinsic_value = max(0, strike_price - spot_price)
            profit_loss = (intrinsic_value - premium) * total_units
            break_even = strike_price - premium
        
        return {
            "profit_loss": round(profit_loss, 2),
            "break_even": round(break_even, 2),
            "total_premium_paid": round(total_premium, 2),
            "oi_insight": "OI data unavailable. High OI at strike may indicate support/resistance."
        }
    
    except Exception as e:
        return {"error": f"Calculation error: {str(e)}"}
```
