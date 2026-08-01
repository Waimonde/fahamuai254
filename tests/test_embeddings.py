from app.embeddings import embedding_service


def main():

    print("=" * 60)
    print("FAHAMU AI 254 - EMBEDDINGS TEST")
    print("=" * 60)

    embeddings = embedding_service.get_embeddings()

    vector = embeddings.embed_query("Hello Fahamu AI")

    print(f"\nEmbedding dimensions: {len(vector)}")
    print("\nFirst 10 values:")
    print(vector[:10])

    print("\n✓ Embedding model is working!")


if __name__ == "__main__":
    main()