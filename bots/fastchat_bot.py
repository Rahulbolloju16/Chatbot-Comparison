# bots/fastchat_bot.py

from bots.base_bot import BaseBot

class FastChatBot(BaseBot):
    def __init__(self, documents_path: str):
        super().__init__(documents_path)
        # Placeholder: Implement your local LLM server interaction here
        # For example, via REST API or subprocess calls

    def answer(self, question: str) -> str:
        # Replace with actual interaction logic with your FastChat server
        return "FastChatBot response placeholder."
