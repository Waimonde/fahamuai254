from ingest.ingest import ingestion_pipeline


def main():

    chunks = ingestion_pipeline.run()

    print("\n" + "=" * 60)
    print(f"Successfully indexed {chunks} chunk(s).")
    print("=" * 60)


if __name__ == "__main__":
    main()