from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)