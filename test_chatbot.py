from groq import Groq

client = Groq(
    api_key="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"
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is Artificial Intelligence?",
        }
    ],
    model="llama-3.1-8b-instant",
)

print(chat_completion.choices[0].message.content)