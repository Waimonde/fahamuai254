"""
Chat Service

Maintains conversation history and
communicates with the RAG engine.
"""

from app.rag import rag_service


class ChatService:

    def __init__(self):

        self.history = []

    def ask(self, question):

        answer, sources = rag_service.ask(question)

        self.history.append(
            {
                "question": question,
                "answer": answer
            }
        )

        return answer, sources

    def get_history(self):

        return self.history

    def clear_history(self):

        self.history.clear()


chat_service = ChatService()