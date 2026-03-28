import json
import os

MEMORY_FILE = "conversation_memory.json"

if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, 'w') as f:
        json.dump({"History": []}, f)


def save_to_memory(user_input, assistant_response):
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)
    memory["History"].append({"User": user_input, "Assistant": assistant_response})

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)


def get_recent_memory(n=5):
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)
    return memory["History"][-n:]



