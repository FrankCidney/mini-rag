import re
from dataclasses import dataclass

from documents import Chunk

@dataclass
class SearchResult:
    chunk: Chunk
    score: int

def tokenize(text: str) -> set[str]:
    words = re.findall(r"\b\w+\b", text.lower())
    return set(words)

def search_chunks(
        query: str,
        chunks: list[Chunk],
        top_k: int = 3,
) -> list[SearchResult]:
    query_words = tokenize(query)

    results: list[SearchResult] = []

    for chunk in chunks:
        chunk_words = tokenize(chunk.text)

        matching_words = query_words.intersection(chunk_words)
        score = len(matching_words)

        if score > 0:
            results.append(
                SearchResult(
                    chunk=chunk,
                    score=score
                )
            )

    results.sort(
        key=lambda result: result.score,
        reverse=True,
    )

    return results[:top_k]

