"""
Vector Store Service for Fahamu AI 254

Uses ChromaDB to store and retrieve document embeddings.
"""

from langchain_chroma import Chroma

from app.embeddings import embedding_service


class VectorStoreService:

    def __init__(self):

        self.persist_directory = "vector_store"

        self.db = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=embedding_service.get_embeddings()
        )

    def get_db(self):
        return self.db


# Singleton instance
vectorstore_service = VectorStoreService()