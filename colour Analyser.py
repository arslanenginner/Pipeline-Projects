

!pip install openai

import openai

import os
import openai

openai.api_key = os.getenv("your api key")
def colour_analyser(text):
  response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with a description of a mood, and your task is to generate the CSS code for a color that matches it. Write your output in json with a single key called \"css_code\"."
    },
    {
      "role": "user",
      "content": "Blue sky at dusk."
    }
  ],
  temperature=0,
  max_tokens=1024
)
  response_text = response.choices[0].message.content.strip().lower()

  return response_text
  input= "sky is blue"
  response=colour_analyser(input)
  print(input)

