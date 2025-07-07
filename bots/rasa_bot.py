# bots/rasa_bot.py

from bots.base_bot import BaseBot

class RasaBot(BaseBot):
    def __init__(self, documents_path: str):
        super().__init__(documents_path)
        # Assume Rasa server is running locally on port 5005
        self.url = "http://localhost:5005/model/parse"

    def answer(self, question: str) -> str:
        # Here, you’d call your Rasa server for intent and entities
        # For demo, just echo back question
        # You can extend to call Rasa endpoint and map intents to answers
        return f"RasaBot response placeholder for: {question}"
