from app.retriever import retriever_service


def main():

    print("=" * 60)
    print("FAHAMU AI 254 - RETRIEVER TEST")
    print("=" * 60)

    question = "Who is a data controller?"

    print(f"\nQuestion:\n{question}")

    documents = retriever_service.retrieve(question)

    print(f"\nRetrieved {len(documents)} chunk(s).\n")

    for i, doc in enumerate(documents, start=1):

        print("=" * 60)
        print(f"Chunk {i}")
        print("=" * 60)

        print(doc.page_content[:600])

        print("\nMetadata:")
        print(doc.metadata)
        print()


if __name__ == "__main__":
    main()