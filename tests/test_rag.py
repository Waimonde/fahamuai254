from app.rag import rag_service


def main():

    print("=" * 60)
    print("FAHAMU AI 254 - RAG TEST")
    print("=" * 60)

    question = input("\nAsk a question: ")

    answer, documents = rag_service.ask(question)

    print("\n" + "=" * 60)
    print("ANSWER")
    print("=" * 60)

    print(answer)

    print("\n" + "=" * 60)
    print("SOURCES")
    print("=" * 60)

    for i, doc in enumerate(documents, start=1):

        print(
            f"{i}. {doc.metadata.get('source')} "
            f"(Page {doc.metadata.get('page')})"
        )


if __name__ == "__main__":
    main()
