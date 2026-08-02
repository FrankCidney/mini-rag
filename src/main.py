from pathlib import Path
from documents import chunk_documents, load_documents

def main() -> None:
    data_directory = Path(__file__).parent.parent / "data"

    documents = load_documents(data_directory)
    chunks = chunk_documents(documents)

    print(f"Loaded {len(documents)} documents")
    print(f"Created {len(chunks)} chunks")

    for chunk in chunks:
        print("\n" + "=" * 60)
        print(f"Chunk ID: {chunk.id}")
        print(f"Source: {chunk.filename}")
        print(f"Position: {chunk.position}")
        print("-" * 60)
        print(chunk.text)

if __name__ == "__main__":
    main()