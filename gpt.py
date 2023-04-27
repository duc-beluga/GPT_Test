import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_KEY")

prompt = "Will this API generate the same message as chatGPT?"
response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=50)
output = response.choices[0].text
print(output)
