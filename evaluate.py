# evaluate.py

import json
import time
from sentence_transformers import SentenceTransformer, util  # type: ignore

from bots.openai_bot import OpenAIBot
from bots.langchain_bot import LangChainBot
from bots.llamaindex_bot import LlamaIndexBot
from bots.haystack_bot import HaystackBot
from bots.fastchat_bot import FastChatBot
from bots.rasa_bot import RasaBot
from bots.dialogflow_bot import DialogflowBot
from bots.botpress_bot import BotpressBot
from bots.witai_bot import WitAIBot

DOCUMENTS_PATH = "data/knowledge_base"
TEST_SET_PATH = "datasets/test_questions.json"

# Load sentence transformer model for semantic similarity
model = SentenceTransformer('all-MiniLM-L6-v2')

# Instantiate all bots with documents path
bots = [
    OpenAIBot(DOCUMENTS_PATH),
    LangChainBot(DOCUMENTS_PATH),
    LlamaIndexBot(DOCUMENTS_PATH),
    HaystackBot(DOCUMENTS_PATH),
    FastChatBot(DOCUMENTS_PATH),
    RasaBot(DOCUMENTS_PATH),
    DialogflowBot(DOCUMENTS_PATH),
    BotpressBot(DOCUMENTS_PATH),
    WitAIBot(DOCUMENTS_PATH),
]

# Load test questions and expected answers
with open(TEST_SET_PATH, "r", encoding="utf-8") as f:
    test_set = json.load(f)

print("\n📊 Chatbot Comparison Results:\n")

for bot in bots:
    print(f"\n--- Testing {bot.name()} ---")
    total_exact = 0
    total_semantic = 0
    start_time = time.time()

    for item in test_set:
        question = item["question"]
        expected = item["expected_answer"]

        try:
            pred = bot.answer(question)
        except Exception as e:
            pred = f"Error: {str(e)}"

        # Exact match: simple lowercase equality
        exact_match = int(pred.strip().lower() == expected.strip().lower())

        # Semantic similarity (cosine similarity between embeddings)
        semantic_sim = util.cos_sim(model.encode(pred), model.encode(expected))[0][0].item()

        total_exact += exact_match
        total_semantic += semantic_sim

        print(f"Q: {question}")
        print(f"Predicted: {pred}")
        print(f"Expected: {expected}")
        print(f"Exact Match: {exact_match} | Semantic Similarity: {semantic_sim:.3f}")
        print("-" * 40)

    duration = time.time() - start_time
    print(f"\nExact Match Accuracy: {total_exact}/{len(test_set)}")
    print(f"Average Semantic Similarity: {total_semantic / len(test_set):.3f}")
    print(f"Total Time: {duration:.2f} seconds")
    print("="*60)
