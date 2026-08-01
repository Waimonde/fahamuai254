"""
Ingestion Pipeline

Reads documents, splits them into chunks,
and stores them in ChromaDB.
"""

from ingest.loader import document_loader
from ingest.splitter import document_splitter
from app.vectorstore import vectorstore_service


class IngestionPipeline:

    def __init__(self):

        self.loader = document_loader
        self.splitter = document_splitter
        self.vector_db = vectorstore_service.get_db()

    def run(self):

        print("=" * 60)
        print("FAHAMU AI 254 - INGESTION PIPELINE")
        print("=" * 60)

        # Step 1
        print("\nStep 1: Loading documents...")
        documents = self.loader.load_documents()

        print(f"Loaded {len(documents)} page(s).")

        # Step 2
        print("\nStep 2: Splitting documents...")
        chunks = self.splitter.split_documents(documents)

        print(f"Generated {len(chunks)} chunk(s).")

        # Step 3
        print("\nStep 3: Creating embeddings and storing in ChromaDB...")

        self.vector_db.add_documents(chunks)

        print("Documents stored successfully!")

        print("\nIngestion completed successfully!")

        return len(chunks)


ingestion_pipeline = IngestionPipeline()