# bots/haystack_bot.py

from bots.base_bot import BaseBot
import os
from haystack.document_stores import FAISSDocumentStore # type: ignore
from haystack.nodes import DensePassageRetriever, FARMReader, TransformersReader, EmbeddingRetriever # type: ignore
from haystack.pipelines import ExtractiveQAPipeline # type: ignore
from haystack.utils import clean_wiki_text # type: ignore

class HaystackBot(BaseBot):
    def __init__(self, documents_path: str):
        super().__init__(documents_path)
        self.document_store = FAISSDocumentStore(faiss_index_factory_str="Flat")
        self._load_documents()
        self.retriever = DensePassageRetriever(document_store=self.document_store)
        self.document_store.update_embeddings(self.retriever)
        self.reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=False)
        self.pipe = ExtractiveQAPipeline(reader=self.reader, retriever=self.retriever)

    def _load_documents(self):
        docs = []
        for filename in sorted(os.listdir(self.documents_path)):
            if filename.endswith(".txt"):
                with open(os.path.join(self.documents_path, filename), "r", encoding="utf-8") as f:
                    text = f.read()
                    docs.append({"content": text, "meta": {"name": filename}})
        self.document_store.write_documents(docs)

    def answer(self, question: str) -> str:
        prediction = self.pipe.run(query=question, params={"Retriever": {"top_k": 5}, "Reader": {"top_k": 1}})
        answers = prediction.get("answers", [])
        if answers:
            return answers[0].answer
        return "No answer found."
