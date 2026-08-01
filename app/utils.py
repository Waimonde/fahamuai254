"""
Utility functions for Fahamu AI 254.
"""

from langchain_core.documents import Document


def format_documents(documents: list[Document]) -> str:
    """
    Combine retrieved documents into a single context string.

    Args:
        documents: List of LangChain Document objects.

    Returns:
        A formatted string containing all retrieved document text.
    """

    return "\n\n".join(doc.page_content for doc in documents)