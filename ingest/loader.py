"""
Document Loader

Reads PDF files from the knowledge base.
"""

from pathlib import Path

from langchain_community.document_loaders import PyMuPDFLoader


class DocumentLoader:

    def __init__(self, knowledge_base="knowledge_base"):
        self.knowledge_base = Path(knowledge_base)

    def load_documents(self):

        documents = []

        pdf_files = list(self.knowledge_base.glob("*.pdf"))

        print(f"\nFound {len(pdf_files)} PDF(s).")

        for pdf in pdf_files:

            print(f"Loading: {pdf.name}")

            loader = PyMuPDFLoader(str(pdf))

            documents.extend(loader.load())

        return documents


document_loader = DocumentLoader()