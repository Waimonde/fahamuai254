"""
Embedding Service for Fahamu AI 254

Uses Ollama's local embedding model.
"""

from langchain_ollama import OllamaEmbeddings


class EmbeddingService:
    def __init__(self):
        self.embeddings = OllamaEmbeddings(
            model="nomic-embed-text"
        )

    def get_embeddings(self):
        return self.embeddings


# Singleton instance
embedding_service = EmbeddingService()