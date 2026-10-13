from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any

from langchain_text_splitters import RecursiveCharacterTextSplitter


class ChunkingError(Exception):
    """Raised when document chunking fails."""


def clean_text(text: str) -> str:
    """Normalize common text-extraction artifacts without destroying paragraphs."""
    text = text.replace("\x00", "")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def chunk_document(
    text: str,
    document_id: str,
    source: str,
    tenant_id: str,
    chunk_size: int = 500,
    chunk_overlap: int = 75,
) -> list[dict[str, Any]]:
    if not text or not text.strip():
        raise ChunkingError("Document contains no usable text.")

    if chunk_size <= 0:
        raise ChunkingError("chunk_size must be positive.")

    if chunk_overlap < 0 or chunk_overlap >= chunk_size:
        raise ChunkingError(
            "chunk_overlap must be >= 0 and smaller than chunk_size."
        )

    cleaned = clean_text(text)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
        length_function=len,
        add_start_index=True,
    )

    documents = splitter.create_documents(
        texts=[cleaned],
        metadatas=[{
            "document_id": document_id,
            "source": source,
            "tenant_id": tenant_id,
        }],
    )

    chunks = []

    for index, document in enumerate(documents):
        chunk_text = document.page_content
        start_index = document.metadata.get("start_index", 0)

        chunk_id = hashlib.sha256(
            f"{document_id}:{index}:{chunk_text}".encode("utf-8")
        ).hexdigest()[:16]

        chunks.append({
            "chunk_id": chunk_id,
            "text": chunk_text,
            "metadata": {
                **document.metadata,
                "chunk_index": index,
                "start_index": start_index,
                "char_count": len(chunk_text),
            },
        })

    return chunks


def main() -> None:
    sample = """
    Amazon Bedrock provides access to foundation models.

    Applications should handle throttling with exponential backoff.
    Retry attempts should be bounded and include jitter.

    Retrieval quality depends on chunk boundaries and metadata.
    """

    chunks = chunk_document(
        text=sample,
        document_id="doc-001",
        source="bedrock-guide.txt",
        tenant_id="tenant-42",
        chunk_size=100,
        chunk_overlap=20,
    )

    for chunk in chunks:
        print(f"\nChunk ID: {chunk['chunk_id']}")
        print(f"Text: {chunk['text']}")
        print(f"Metadata: {chunk['metadata']}")


if __name__ == "__main__":
    main()