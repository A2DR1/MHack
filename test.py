from openai import OpenAI

client = OpenAI(api_key="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")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "/Users/austinshen/Documents/Umich/MHack/Web/data/dog.png",
                    }
                },
            ],
        }
    ],
    max_tokens=300,
)

print(response.choices[0])