from dotenv import load_dotenv
import os
load_dotenv()


import streamlit as st
from price_tracker import check_price
from email_drafter import generate_email

st.title("🕵️ AI Deal Hunter & Negotiator Bot")

product = st.text_input("Enter product name")
current_price = st.number_input("Enter current price", min_value=0.0)
target_price = st.number_input("Enter your target price", min_value=0.0)

if st.button("Check Deal"):
    is_good_deal = check_price(current_price, target_price)
    if is_good_deal:
        st.success("Great deal! Let's draft a negotiation email.")
        email = generate_email(product, current_price, target_price)
        st.code(email)
    else:
        st.warning("Not a great deal yet. Try again later.")
