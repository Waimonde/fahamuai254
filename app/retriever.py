"""
Retriever Service

Retrieves the most relevant document chunks
from the vector database.
"""

from app.vectorstore import vectorstore_service


class RetrieverService:

    def __init__(self):

        self.db = vectorstore_service.get_db()

        self.retriever = self.db.as_retriever(
            search_kwargs={"k": 4}
        )

    def retrieve(self, question):

        return self.retriever.invoke(question)


retriever_service = RetrieverService()