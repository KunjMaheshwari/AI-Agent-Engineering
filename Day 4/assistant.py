from openai import OpenAI 
from dotenv import load_dotenv 
import os
from tools import (get_current_time, roll_dice, generate_password)

load_dotenv()

client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))

print("="*40)
print("My AI Assistant")
print("="*40)

roles = {
    "1": "You are a friendly AI teacher. Explain every concept in a simple and easy-to-understand manner.",
    "2": "You are a professional software engineer. Provide detailed technical explanations and code examples.",
    "3": "You are a creative storyteller. Craft engaging and imaginative stories based on user prompts.",
    "4": "You are a helpful assistant. Provide concise and accurate information to help the user with their queries.",
    "5": "You are a motivational coach. Inspire and encourage the user to achieve their goals and overcome challenges."
}

print("Select a role for the AI assistant:")
for key, value in roles.items():
    print(f"{key}. {value}")

selected_role = input("Enter the number of your chosen role: ")

if selected_role in roles:
    messages = [
        {
            "role": "system",
            "content": roles[selected_role]
        }
    ]
else:
    print("Invalid selection. Using default role.")
    messages = [
        {
            "role": "system",
            "content": "You are a friendly AI teacher. Explain every concept in a simple and easy-to-understand manner."
    }
]

while True:
    user_input = input("You: ")
    if(user_input.lower() == "time"):
        print("Current Time:", get_current_time())
        continue
    elif(user_input.lower() == "roll"):
        print("Rolling a die:", roll_dice())
        continue
    elif(user_input.lower().startswith("password")):
        try:
            length = int(user_input.split()[1])
            print("Generated Password:", generate_password(length))
        except (IndexError, ValueError):
            print("Please provide a valid length for the password. Example: 'password 12'")
        continue
    messages.append({"role": "user", "content": user_input})
    
    print("\nProcessing your request...\n")
    for message in messages:
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

