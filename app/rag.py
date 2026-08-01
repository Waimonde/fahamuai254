"""
Retrieval-Augmented Generation (RAG) Engine

Coordinates retrieval and answer generation.
"""

from app.llm import llm_service
from app.retriever import retriever_service
from app.utils import format_documents


class RAGService:

    def __init__(self):
        self.llm = llm_service
        self.retriever = retriever_service

    def ask(self, question: str):

        # Step 1: Retrieve relevant documents
        documents = self.retriever.retrieve(question)

        # Step 2: Format retrieved context
        context = format_documents(documents)

        # Step 3: Build the prompt
        prompt = f"""
You are Fahamu AI 254.

Answer the user's question ONLY using the context below.

If the answer is not contained in the context, say:

"I couldn't find that information in the knowledge base."

Context:
{context}

Question:
{question}

Answer:
"""

        # Step 4: Generate answer
        answer = self.llm.ask(prompt)

        return answer, documents


rag_service = RAGService()