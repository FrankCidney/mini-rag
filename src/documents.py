from dataclasses import dataclass
from pathlib import Path

@dataclass
class Document:
    filename: str
    text: str

@dataclass
class Chunk:
    id: int
    filename: str
    text: str
    position: int

def load_documents(directory: Path) -> list[Document]:
    documents: list[Document] = []

    for path in sorted(directory.glob("*.txt")):
        text = path.read_text(encoding="utf-8")

        documents.append(
            Document(
                filename=path.name,
                text=text,
            )
        )

    return 

def chunk_document(
        document: Document,
        starting_id: int,
        paragraphs_per_chunk: int = 1,
) -> list[Chunk]:
    paragraphs = [
        paragraph.strip()
        for paragraph in document.text.split("\n\n")
        if paragraph.strip()
    ]

    chunks: list[Chunk] = []

    for position in range(0, len(paragraphs), paragraphs_per_chunk):
       selected_paragraphs = paragraphs[
           position: position + paragraphs_per_chunk
       ]

       chunk_text = "\n\n".join(selected_paragraphs)

       chunks.append(
           Chunk(
               id=starting_id + len(chunks),
               filename=document.filename,
               text=chunk_text,
               position=position,
           )
       )

       return chunks

def chunk_documents(documents: list[Document]) -> list[Chunk]:
    chunks: list[Chunk] = []

    for document in documents:
        document_chunks = chunk_document(
            document=document,
            starting_id=len(chunks),
        )

        chunks.extend(document_chunks)

    return chunks
