from ingest.loader import document_loader


def main():

    print("=" * 60)
    print("FAHAMU AI 254 - DOCUMENT LOADER TEST")
    print("=" * 60)

    docs = document_loader.load_documents()

    print(f"\nLoaded {len(docs)} pages.")

    if docs:

        print("\nFirst document preview:\n")

        print(docs[0].page_content[:500])


if __name__ == "__main__":
    main()