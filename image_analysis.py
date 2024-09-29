import base64
import requests

# OpenAI API Key
api_key = "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"

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def analyze_image_with_gpt4(image_path):
  # Getting the base64 string
  base64_image = encode_image(image_path)

  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }

  payload = {
    "model": "gpt-4o-mini",
    "messages": [
      {
        "role": "system",
        "content": "You need to find out all the ingredients that could be used for cooking. Seperate each of them with a new line. Answer in consistent style."
      },
      {
        "role": "assistant",
        "content": "Apple, Banana, Chicken"
      },
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "This is an image of a fridge, please list the ingredients inside it in a list."
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          }
        ]
      }
    ],
    "max_tokens": 300
  }
  response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
  return response.json()['choices'][0]['message']['content']
