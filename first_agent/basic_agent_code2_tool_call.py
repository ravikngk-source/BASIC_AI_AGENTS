import google.generativeai as genai
import json
from basic_agent_code2 import get_current_time
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")   

if not API_KEY:
    raise ValueError("API key not found. Please set the GEMINI_API_KEY environment variable.")  

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("models/gemini-2.5-flash")    

def agent_with_API_calls(prompt):
    try:
        if "time" in prompt.lower():
            current_time = get_current_time()
            prompt += f"\nThe current time in Asia/Kolkata is: {current_time}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("An error occurred:", str(e)) 
        return "Error occurred while generating content."   
    
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    result = agent_with_API_calls(user_prompt)
    print("Agent Response:", result)