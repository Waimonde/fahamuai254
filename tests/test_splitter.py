from ingest.loader import document_loader
from ingest.splitter import document_splitter


def main():

    print("=" * 60)
    print("FAHAMU AI 254 - SPLITTER TEST")
    print("=" * 60)

    documents = document_loader.load_documents()

    chunks = document_splitter.split_documents(documents)

    print(f"\nOriginal Pages : {len(documents)}")
    print(f"Generated Chunks : {len(chunks)}")

    print("\nFirst Chunk:\n")
    print(chunks[0].page_content[:500])

    print("\nMetadata:")
    print(chunks[0].metadata)


if __name__ == "__main__":
    main()