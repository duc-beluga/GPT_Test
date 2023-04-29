import openai
from dotenv import load_dotenv
import os


def chatGPT(chat_prompt):
    load_dotenv()

    openai.api_key = os.getenv("OPENAI_KEY")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": chat_prompt},
        ],
    )
    return response.choices[0].message.content


# output = response.choices[0].text
