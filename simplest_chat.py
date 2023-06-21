import openai

openai.api_key = 'xxxxxxxxxxxx'

model = "gpt-3.5-turbo"

messages =  [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "How do I check my python version?"}
            ]

response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=0.84,
)

message = response['choices'][0]['message']['content']

print(message)
