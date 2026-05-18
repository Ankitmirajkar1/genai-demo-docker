from fastapi import FastAPI
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Initialize Groq client with API key from environment variable
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.get("/")
def home():
    return {"message": "Welcome to the GenAI API!. GenAI docker demo is running successfully."}

## AI endpoint to generate text based on a prompt
@app.get("/ask")
def ask_ai(question: str):

    response = client.chat.completions.create(
        model = "openai/gpt-oss-120b",
        messages = [
            {
                "role": "user",
                "content": question
            }
        ]
    )

    answer = response.choices[0].message.content

    return {"question": question, 
            "answer": answer}