from app.chat import chat_service


def main():

    print("=" * 60)
    print("FAHAMU AI 254 CHAT")
    print("=" * 60)

    while True:

        question = input("\nYou: ")

        if question.lower() == "exit":
            break

        answer, sources = chat_service.ask(question)

        print("\nAI:")
        print(answer)

        print("\nSources:")

        for source in sources:

            print(
                f"- {source.metadata.get('source')} "
                f"(Page {source.metadata.get('page')})"
            )


if __name__ == "__main__":
    main()