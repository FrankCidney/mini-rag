from pathlib import Path

from documents import chunk_documents, load_documents
# from retrieval import search_chunks
from vectors import build_vocabulary, vectorize

def main() -> None:
    data_directory = Path(__file__).parent.parent / "data"

    documents = load_documents(data_directory)
    chunks = chunk_documents(documents)

    vocabulary = build_vocabulary(chunks)

    print(f"Loaded {len(documents)} documents")
    print(f"Created {len(chunks)} chunks")
    print(f"Vocabulary size: {len(vocabulary)}")

    print("\nFirst 20 vocabulary words:")
    print(vocabulary[:20])

    query = input("\nEnter a question: ").strip()

    query_vector = vectorize(
        text=query,
        vocabulary=vocabulary
    )

    print("\nQuery:")
    print(query)

    print("\nQuery vector:")
    print(query_vector)

    print("\nNon-zero vector positions:")

    for index, count in enumerate(query_vector):
        if count > 0:
            print(
                f"Index {index}: "
                f"word]'{vocabulary[index]}', "
                f"count={count}"
            )

    # while True:
    #     print()
    #     query = input("Ask a question, or type 'exit': ").strip()

    #     if query.lower() == "exit":
    #         break

    #     if not query:
    #         print("Please enter a question.")
    #         continue

    #     results = search_chunks(
    #         query=query,
    #         chunks=chunks,
    #         top_k=3,
    #     )

    #     if not results:
    #         print("No matching chunks found.")
    #         continue

    #     print("\nTop results:")

    #     for number, result in enumerate(results, start=1):
    #         print("\n" + "=" * 60)
    #         print(f"Result: {number}")
    #         print(f"Score: {result.score}")
    #         print(f"Source: {result.chunk.filename}")
    #         print(f"Chunk ID: {result.chunk.id}")
    #         print(f"Position: {result.chunk.position}")
    #         print("-" * 60)
    #         print(result.chunk.text)

if __name__ == "__main__":
    main()