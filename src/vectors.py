import re

from documents import Chunk

STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "can",
    "do",
    "for",
    "from",
    "how",
    "i",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "the",
    "to",
    "what",
    "when",
    "where",
    "who",
    "with",
}

def tokenize(text: str) -> list[str]:
    words = re.findall(r"\b\w+\b", text.lower)

    return [
        word
        for word in words
        if word not in STOP_WORDS
    ]

def build_vocabulary(chunks: list[Chunk]) -> list[str]:
    vocabulary: set[str] = set()

    for chunk in chunks:
        words = tokenize(chunk.text)
        vocabulary.update(words)

    return sorted(vocabulary)

def vectorize(text: str, vocabulary: list[str]) -> list[int]:
    words = tokenize(text)

    vector: list[int] = []

    for vocabulary_word in vocabulary:
        count = words.count(vocabulary_word) 
        vector.append(count)

    return vector