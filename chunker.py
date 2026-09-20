"""
Stage 2 of the pipeline: splitting documents into chunks.

Milestone 3:
For the campus_life corpus, the documents are already short and usually
focus on one topic. Because of this, each document is kept as one complete
chunk instead of splitting it at a fixed character count.
"""

from dataclasses import dataclass

import config
from ingest import Document


@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"


def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker.
    Fixed-size character windows with overlap.

    Keep this function so we can compare our custom strategy
    with the original strategy later.
    """

    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []

    for doc in documents:
        start = 0
        index = 0

        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()

            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )

                index += 1

            start += chunk_size - overlap

    return chunks


def split_documents(documents: list[Document]) -> list[Chunk]:
    """
    Custom chunking strategy for the campus_life corpus.

    The campus_life documents are short posts and usually contain one
    main topic. Keeping each document as one chunk preserves the complete
    thought and avoids splitting useful information in the middle.
    """

    chunks: list[Chunk] = []

    for doc in documents:
        text = doc.text.strip()

        if text:
            chunks.append(
                Chunk(
                    text=text,
                    source=doc.source,
                    index=0,
                    produced_by="chunker.py::split_documents",
                )
            )

    return chunks


def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""

    if not chunks:
        return "0 chunks"

    lengths = [len(c.text) for c in chunks]

    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))