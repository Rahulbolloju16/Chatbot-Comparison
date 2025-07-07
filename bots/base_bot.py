# bots/base_bot.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# (rest of the code follows)
class BaseBot:
    def __init__(self, documents_path: str):
        self.documents_path = documents_path

    def answer(self, question: str) -> str:
        raise NotImplementedError("Subclasses must implement this method")

    def name(self) -> str:
        return self.__class__.__name__


# ----------------- Testing block -------------------
if __name__ == "__main__":
    # A dummy subclass for testing BaseBot
    class DummyBot(BaseBot):
        def answer(self, question: str) -> str:
            return f"Answered: {question}"

    # Instantiate and test
    bot = DummyBot("test/documents/path")
    print(f"Bot Name: {bot.name()}")
    print(bot.answer("What is AI?"))

    # Expected Output:
    # Bot Name: DummyBot
    # Answered: What is AI?
