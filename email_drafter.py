# OLD
# from langchain.llms import OpenAI

# NEW
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key  = os.getenv("OPENAI_API_KEY")           # Together.ai key
base_url = os.getenv("OPENAI_API_BASE",          # https://api.together.xyz/v1
                     "https://api.together.xyz/v1")

def generate_email(product, current_price, target_price):
    system_prompt = (
        "You are an expert negotiator. Draft a concise, friendly "
        "email asking a seller for a discount."
    )
    user_prompt = (
        f"Product: {product}\n"
        f"Current price: £{current_price}\n"
        f"Target price: £{target_price}"
    )

    chat = ChatOpenAI(
        api_key     = api_key,
        base_url    = base_url,
        model_name  = "mistralai/Mixtral-8x7B-Instruct-v0.1",
        temperature = 0.7,
    )

    response = chat.invoke([{"role": "system", "content": system_prompt},
                            {"role": "user",   "content": user_prompt}])
    return response.content
