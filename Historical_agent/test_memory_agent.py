from agent_with_memory import ai_agent_with_memory

print("Welcome to the AI Agent with Memory!")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    assistant_response = ai_agent_with_memory(user_input)
    print(f"Assistant: {assistant_response}")