from openai import OpenAI

with open("key.cfg", "r") as file:
    api_key = file.read()

client = OpenAI(api_key=api_key)

model = "gpt-4-1106-preview"

message = "Respond with a paragraph suitable for a reading exercise for a person learning to read. "

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