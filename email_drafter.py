from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Correct variable names
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_api_base = os.getenv("OPENAI_API_BASE")  # optional, if using Together.ai

def generate_email(product, current_price, target_price):
    prompt = f"""
    Draft a polite negotiation email to a seller asking for a discount on a product.
    Product: {product}
    Current Price: £{current_price}
    Target Price: £{target_price}
    Keep it concise and friendly.
    """

    # Fix: Use openai_api_key= instead of api_key=
    chat = ChatOpenAI(
        openai_api_key=openai_api_key,
        openai_api_base=openai_api_base,  # optional, only if needed
        model_name="gpt-3.5-turbo",  # or another model available to your key
        temperature=0.7
    )

    return chat.invoke(prompt)

