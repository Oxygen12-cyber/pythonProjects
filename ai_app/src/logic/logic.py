import os

from dotenv import load_dotenv
from google import genai

load_dotenv()
key = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=key)

# response = client.models.generate_content(
#     model="gemini-2.5-flash", contents="Explain how AI works in a few words"
# )
# print(response.text)

class send_response():
    def __init__(self, message:str):
        self.model="gemini-2.5-flash"
        self.contents=message

        self.response = client.models.generate_content(
            model=self.model, contents=self.contents
        )
    
    def __repr__(self):
        return f"{self.response.text}"
    

chat = send_response("Are you an AI?")
print(chat)