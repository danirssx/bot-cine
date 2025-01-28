# 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
from openai import OpenAI
import requests
import json
from keys import KEY_OPENAI

client = OpenAI(api_key=KEY_OPENAI)

product = "REEFLO® PREMIUM PUMPS – DART-SNAPPER HYBRID 4200-2600 GPH EXTERNAL PUMP"

def completion_chat(product="bread"):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an AI assistant."},
            {
                "role": "user",
                "content": f"""
                                Generate a correct JSON object that will process with json.loads() and provide ' instead of ` in python with the following structure:
                                {{
                                    "query": "The product name formatted for a Google image search query",
                                    "description": "A professional, and serious description of the product for a store."
                                }}

                                Product: {product}

                                Please ensure the response is only the JSON object, with no additional text or explanation. Also always give me a product, try to match the prompt to the product that you think that it's real.
                            """
            }
        ],
        temperature=0.5,
        max_tokens=150,
    )
    # Extract and print the JSON response
    completion_text = completion.choices[0].message.content
    print(completion_text)
    print(type(completion_text))

    # Optionally parse the JSON into a Python dictionary
    result = ""
    if(completion_text):
        result = json.loads(completion_text)

    with open("output.json", 'w') as file:
        json.dump(result, file, indent=4)

    return result
