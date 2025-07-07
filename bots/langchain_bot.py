# bots/langchain_bot.py

from bots.base_bot import BaseBot
# from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter # type: ignore
# from langchain.vectorstores import FAISS
# from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA # type: ignore
# from langchain.llms import OpenAI

from langchain_community.document_loaders import TextLoader # type: ignore
from langchain_community.vectorstores import FAISS # type: ignore
from langchain_community.embeddings import OpenAIEmbeddings # type: ignore
from langchain_community.llms import OpenAI # type: ignore


import os

class LangChainBot(BaseBot):
    def __init__(self, documents_path: str):
        super().__init__(documents_path)
        self.qa_chain = self._build_qa_chain()

    def _build_qa_chain(self):
        # Load docs
        docs = []
        for filename in sorted(os.listdir(self.documents_path)):
            if filename.endswith(".txt"):
                loader = TextLoader(os.path.join(self.documents_path, filename))
                docs.extend(loader.load())

        # Split docs
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_documents(docs)

        # Create vector store
        embeddings = OpenAIEmbeddings()
        vector_store = FAISS.from_documents(chunks, embeddings)

        # Create retrieval QA chain
        llm = OpenAI(temperature=0)
        return RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vector_store.as_retriever())

    def answer(self, question: str) -> str:
        return self.qa_chain.run(question)
