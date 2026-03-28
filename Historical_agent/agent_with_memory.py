import google.generativeai as genai
import os
from memory_manager import save_to_memory, get_recent_memory
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))   
model = genai.GenerativeModel("models/gemini-2.5-flash")

def ai_agent_with_memory(user_input):
    past_conversations = get_recent_memory(3)

    memory_test = ""
    for convo_iteration in past_conversations:
        memory_test += f"User: {convo_iteration['User']}\nAssistant: {convo_iteration['Assistant']}\n"

#     final_prompt = f"""
#     You are a helpful assistant. Here is the conversation history between you and the user:\n   {memory_test}
#     Now, the user has said: "{user_input}". Please provide a helpful and relevant response based on the conversation history and the new user input.  
#     If you don't know the answer, say politely you don't know. If you need to ask the user for more information, do so.  

# """

    final_prompt = f"""
    SYSTEM ROLE: You are a personal assistant.
    
    TASK:
    1- Use the conversation history {memory_test} 
    2- User said: "{user_input}". Generate a helpful and relevant response.
    2- Based on history, You can sugeest or offer to help the user with something that you think might be useful for them.
    3- If you don't know the answer, say politely you don't know. 
    If you need to ask the user for more information, do so.
    """
    response = model.generate_content(final_prompt)
    assistant_response = response.text.strip()
    save_to_memory(user_input, assistant_response)
    return assistant_response
