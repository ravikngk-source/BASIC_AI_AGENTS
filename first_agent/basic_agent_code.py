import openai
import requests

def get_weather(location):
    url = f"https://wttr.in/{location}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return "Unable to fetch weather data."

client = openai.OpenAI(
    api_key="AIzaSyAaOp8kvXCoRE4zUQb45laRTCodm939CDo",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def main():
    user_input = input("> ")
    response = client.chat.completions.create(
        model="gemini-3-flash-preview",
        reasoning_effort="low",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    print(f"{response.choices[0].message.content}")


main()

#print(get_weather("Goa"))

#https://wttr.in/mumbai?format=%C+%t