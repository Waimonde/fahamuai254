from app.llm import llm_service


def main():
    print("=" * 60)
    print("FAHAMU AI 254 - QWEN TEST")
    print("=" * 60)

    question = "Introduce yourself."

    print("\nQuestion:")
    print(question)

    answer = llm_service.ask(question)

    print("\nAnswer:\n")
    print(answer)


if __name__ == "__main__":
    main()