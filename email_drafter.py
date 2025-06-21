import streamlit as st
from langchain_openai import ChatOpenAI

openai_api_key = st.secrets["OPENAI_API_KEY"]
openai_api_base = st.secrets["OPENAI_API_BASE"]

def generate_email(product, current_price, target_price):
    prompt = f"""
    Draft a polite negotiation email to a seller asking for a discount on a product.
    Product: {product}
    Current Price: £{current_price}
    Target Price: £{target_price}
    Keep it concise and friendly.
    """

    chat = ChatOpenAI(
        openai_api_key=openai_api_key,
        openai_api_base=openai_api_base,
        model_name="mistralai/Mixtral-8x7B-Instruct-v0.1",
        temperature=0.7
    )

    return chat.invoke(prompt)
