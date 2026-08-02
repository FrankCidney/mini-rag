from pathlib import Path

from documents import chunk_documents, load_documents
from retrieval import search_chunks

def main() -> None:
    data_directory = Path(__file__).parent.parent / "data"

    documents = load_documents(data_directory)
    chunks = chunk_documents(documents)

    print(f"Loaded {len(documents)} documents")
    print(f"Created {len(chunks)} chunks")

    while True:
        print()
        query = input("Ask a question, or type 'exit': ").strip()

        if query.lower() == "exit":
            break

        if not query:
            print("Please enter a question.")
            continue

        results = search_chunks(
            query=query,
            chunks=chunks,
            top_k=3,
        )

        if not results:
            print("No matching chunks found.")
            continue

        print("\nTop results:")

        for number, result in enumerate(results, start=1):
            print("\n" + "=" * 60)
            print(f"Result: {number}")
            print(f"Score: {result.score}")
            print(f"Source: {result.chunk.filename}")
            print(f"Chunk ID: {result.chunk.id}")
            print(f"Position: {result.chunk.position}")
            print("-" * 60)
            print(result.chunk.text)

if __name__ == "__main__":
    main()