
from openai import OpenAI
client = OpenAI(api_key="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")


def generate_normal_recipe_recommendation(prompt):
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {"role": "system", "content": """You are a health assistant. You need to write 3 recipes based on the ingredients provided.
                                seperate each recipe with a new line. Include the ingredients and the steps to make the recipe."""},
      {"role": "user", "content": prompt}
    ],
    max_tokens=600
  )
  return response.choices[0].message.content

def generate_shopping_list(prompt):
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {"role": "system", "content": """You are a health assistant. Generate a shopping list of 5 ingredients that the I should buy to make more healthy meals.
                                    seperate each ingredient with a new line."""},
      {"role": "user", "content": prompt}
    ],
    max_tokens=600
  )
  return response.choices[0].message.content

def generate_healthy_recipe_recommendation(prompt, shopping_list):
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {"role": "system", "content": """You are a health assistant. You need to write 3 healthy recipes based on the ingredients and the shopping list provided.
                                seperate each recipe with a new line. Include the ingredients and the steps to make the recipe."""},
      {"role": "user", "content": prompt + "\n" + shopping_list}
    ],
    max_tokens=600
  )
  return response.choices[0].message.content
