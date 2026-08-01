from app.vectorstore import vectorstore_service


def main():

    print("=" * 60)
    print("FAHAMU AI 254 - VECTOR STORE TEST")
    print("=" * 60)

    db = vectorstore_service.get_db()

    print("\nVector Store Initialized Successfully!")

    print(f"Database Type: {type(db).__name__}")

    print(f"Persist Directory: vector_store")

    print("\n✓ ChromaDB is ready!")


if __name__ == "__main__":
    main()