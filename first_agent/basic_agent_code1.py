import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Please set the GEMINI_API_KEY environment variable.")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("models/gemini-2.5-flash")

def chat_with_my_first_agent(prompt):
    try:
        response = model.generate_content(prompt)
        print("Assistant:", response.text)
    except Exception as e:
        print("An error occurred:", str(e)) 

if __name__ == "__main__":
    user_input = input("Enter User prompt: ")
    chat_with_my_first_agent(user_input)