"""
Document Splitter

Splits documents into smaller chunks for vector search.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentSplitter:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

    def split_documents(self, documents):

        return self.splitter.split_documents(documents)


document_splitter = DocumentSplitter()