import openai
openai.api_key = "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"

prompt = "Hello, my name is "
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=50
)
output = response.choices[0].text
print(output)
