# bots/llamaindex_bot.py

from bots.base_bot import BaseBot
import os
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader, LLMPredictor, PromptHelper # type: ignore
from langchain.chat_models import ChatOpenAI # type: ignore

class LlamaIndexBot(BaseBot):
    def __init__(self, documents_path: str):
        super().__init__(documents_path)
        self.index = self._build_index()

    def _build_index(self):
        max_input_size = 4096
        num_output = 512
        max_chunk_overlap = 20
        prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)
        llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0, model="gpt-4o-mini"))
        documents = SimpleDirectoryReader(self.documents_path).load_data()
        return GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)

    def answer(self, question: str) -> str:
        response = self.index.query(question)
        return response.response.strip()
