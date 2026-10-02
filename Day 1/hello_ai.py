from openai import OpenAI  # type: ignore[import-not-found]
from dotenv import load_dotenv  # type: ignore[import-not-found]
import os

load_dotenv()

client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))
response = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[
        {"role": "user", "content": "What is Claude Code?"}
    ],
)

print(response.choices[0].message.content)