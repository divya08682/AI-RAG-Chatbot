import os
from dotenv import load_dotenv
from groq import Groq

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=api_key)

# Send message
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is Artificial Intelligence?",
        }
    ],
    model="llama-3.1-8b-instant",
)

# Print response
print(chat_completion.choices[0].message.content)