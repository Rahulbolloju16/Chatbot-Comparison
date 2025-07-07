# bots/openai_bot.py

from bots.base_bot import BaseBot
import os
import openai # type: ignore

class OpenAIBot(BaseBot):
    def __init__(self, documents_path: str):
        super().__init__(documents_path)
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.context = self._load_context()

    def _load_context(self) -> str:
        combined = ""
        for filename in sorted(os.listdir(self.documents_path)):
            if filename.endswith(".txt"):
                with open(os.path.join(self.documents_path, filename), "r", encoding="utf-8") as f:
                    combined += f.read() + "\n"
        return combined

    def answer(self, question: str) -> str:
        prompt = f"Answer the question based on the context:\n\n{self.context}\n\nQ: {question}\nA:"
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # or gpt-4, gpt-3.5-turbo
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response.choices[0].message['content'].strip()

# # ----------------- Testing block -------------------
# if __name__ == "__main__":
#     documents_path = "test_docs"  # <- Replace with your actual path

#     # Make sure OPENAI_API_KEY is set in your environment
#     if not os.getenv("OPENAI_API_KEY"):
#         print("⚠️  Please set your OPENAI_API_KEY environment variable before running this test.")
#     elif not os.path.exists(documents_path):
#         print(f"⚠️  The folder '{documents_path}' does not exist. Please create it and add .txt files.")
#     else:
#         bot = OpenAIBot(documents_path)
#         question = "What is the purpose of these documents?"
#         print(f"Bot: {bot.name()}")
#         print("Answer:", bot.answer(question))
