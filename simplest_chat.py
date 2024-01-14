from openai import OpenAI

api_key = 'xxxxxxxxxx'

client = OpenAI(api_key=api_key)

model = "gpt-4-1106-preview"

message = "What is a nice mellow colour?"

messages=   [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": message}
            ]

response = client.chat.completions.create(
  model=model,
  messages=messages,
  temperature=0.82
)

reply = response.choices[0]

reply = reply.message.content

print(reply)