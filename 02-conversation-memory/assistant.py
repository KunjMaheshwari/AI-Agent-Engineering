from openai import OpenAI 
from dotenv import load_dotenv 
import os

load_dotenv()

client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))

print("="*40)
print("My AI Assistant")
print("="*40)
messages = []

while True:
    user_input = input("You: ")
    messages.append({"role": "user", "content": user_input})
    
    print("\nProcessing your request...\n")
    for message in messages:
        # print(message);
        print(f"{message['role'].title()}: {message['content']}")
        print("------------------------");
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the assistant. Goodbye!")
        break

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages,
    )

    print("Assistant:", response.choices[0].message.content)

