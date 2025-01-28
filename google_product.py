from openai.types.beta.threads.image_url_content_block import ImageURL
from open_product import completion_chat
from PIL import Image
from io import BytesIO
from keys import SEARCH_ENGINE_ID, GOOGLE_API_KEY
import requests

query = "REEFLO PREMIUM PUMPS DART-SNAPPER HYBRID 4200-2600 GPH EXTERNAL PUMP"

# Google Custom Search API endpoint
url = f"https://www.googleapis.com/customsearch/v1"

params = {
    "q": query,
    "cx": SEARCH_ENGINE_ID,
    "key": GOOGLE_API_KEY,
    "search_type": "image",
    "num": 2
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    if "items" in data:
        image_url = data["items"][0]["link"]
        print(f"Image URL: {image_url}")

        image_response = requests.get(image_url)

        if image_response.status_code == 200:

            image = Image.open(BytesIO(image_response.content))

            if image.mode == "RGBA":
                background = Image.new("RGB", image.size, (255, 255, 255))  # White background
                background.paste(image, mask=image.split()[3])  # Use alpha channel as mask
                image = background

            image.save(f"{query}.jpg")

            image.show()

        else:
            print("Failed to download thge image")

    else:
        print("No image founded")

else:
    print(f"Error: {response.status_code}, {response.text}")
