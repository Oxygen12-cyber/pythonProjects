import os

from dotenv import load_dotenv
from google import genai

load_dotenv()
key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=key)


class send_response:
    def __init__(self, model: str = "gemini-2.5-flash"):
        self.model = model

    def send(self, message: str):
        self.response = client.models.generate_content(
            model=self.model, contents=message
        )
        return self.response.text

    def __call__(self):
        return self.send

    def __repr__(self):
        return f"{self.response.text}"


chat = send_response.send(message="are you an AI?")
print(chat)

