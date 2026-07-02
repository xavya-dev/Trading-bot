import streamlit as st
from bot.client import BinanceFuturesClient

# Nimma testnet keys illi haaki
API_KEY = "4MJlSQqtKGnWLF5MpvrbV01GnIrwIdsGKRuNIu6L8iu6y7S4SKLmUYNaYwGVJlo7"
API_SECRET = "HdP6kt8CBXlMtBANqJ555NLcQ0lq7L38FNRozLObIWpNBks608UYrobNJDUmeu2N"

def main():
    # Page setup
    st.set_page_config(page_title="Binance Trading Bot", page_icon="🚀")
    
    # Title and description
    st.title("🚀 Binance Trading Bot")
    st.markdown("This is a lightweight UI for the Binance Futures Testnet Bot.")
    st.markdown("---")

    # Initialize bot
    bot = BinanceFuturesClient(API_KEY, API_SECRET)

    # UI Elements (Form)
    col1, col2 = st.columns(2)
    
    with col1:
        symbol = st.text_input("Symbol (e.g., BTCUSDT)", value="BTCUSDT")
        
    with col2:
        side = st.selectbox("Order Side", options=["BUY", "SELL"], index=1)

    quantity = st.number_input("Quantity", value=0.003, format="%f")

    # Submit Button
    if st.button("Place Market Order"):
        try:
            # Assuming your bot client has a method named 'place_market_order' or similar
            # Please change 'place_market_order' if your method name is slightly different in bot/client.py
            response = bot.place_order(symbol=symbol, side=side, order_type="MARKET", qty=quantity)
            
            st.success("Order Placed Successfully!")
            st.json(response)
            
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()