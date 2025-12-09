from openai import OpenAI

client = OpenAI()

response = client.create_comp(
    engine="text-davinci-003",
    prompt="Once upon a time",
    max_tokens=60
)

print(response.choices[0].text)