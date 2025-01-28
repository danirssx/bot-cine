from google_product import google_images
from open_product import completion_chat

product = "KONG® TRAVEL – ULTIMATE BOOSTER SEAT & TETHER"

def bot_product(product=""):
    completion = completion_chat(product)
    # Check if 'query' exists in the completion and handle it
    query = completion.get("query") if isinstance(completion, dict) else None

    if query:
           print(f"Using query: {query}")
           google_images(query)
    else:
           print("Query not found in the completion. Skipping Google Images search.")

bot_product(product)
