import openai
from dotenv import load_dotenv
import os


def extract_content(completion):
    return completion["choices"][0]["message"]["content"]


if __name__ == "__main__":
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    messages = [
        {
            "role": "system",
            "content": "User are a the game master for a Dungeons and Dragons themed roleplaying game. Your goal is to provide a coherent, entertaining, and interative experience. You take the users decisions into account. You try to make things fun. You try to make a coherrent narrative",
        },
        {
            "role": "assistant",
            "content": "Hello. This is a new game. What is your name?",
        },
        {
            "role": "user",
            "content": "Alvic",
        },
        {
            "role": "assistant",
            "content": "Great! And what kind of character is Alvic?",
        },
        {
            "role": "user",
            "content": "He is a wizard, he specializes in fire magic.",
        },
        {
            "role": "assistant",
            "content": "Excellent choice. You are in a forest. You see a path to the left and a path to the right. Which path do you take?",
        },
        {
            "role": "user",
            "content": "Actually, I'd like to start a new character. Also, pretent I'm a different person and re-introduce the game to me.",
        },
    ]

    while True:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )

        ai_response = extract_content(completion)

        print(ai_response)

        player_response = input("You: ")

        messages.extend(
            [
                {
                    "role": "assistant",
                    "content": ai_response,
                },
                {
                    "role": "user",
                    "content": player_response,
                },
            ]
        )
