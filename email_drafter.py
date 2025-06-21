from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
openai_api_base = os.getenv("OPENAI_API_BASE")  # Optional if using Together.ai

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
        openai_api_base=openai_api_base,  # Optional if using Together
        model_name="mistralai/Mixtral-8x7B-Instruct-v0.1",  # Check if this model is supported
        temperature=0.7,
    )

    return chat.invoke(prompt)
