from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_ai(question: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a DevOps and Cloud Engineering tutor. "
                        "Your name is DevOps Bot built by 0xApana. "
                        "Explain concepts clearly and simply using real world analogies. "
                        "Keep answers concise — maximum 200 words. "
                        "Always be encouraging to learners."
                    )
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Sorry I couldn't process that right now. Please try again later. Error: {str(e)}"
