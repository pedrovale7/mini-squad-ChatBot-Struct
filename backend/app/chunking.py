from langchain_text_splitters import RecursiveCharacterTextSplitter
from parser import parse_document

def chunking(text: str) -> list[str]:

    splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", " ", ""],
        chunk_size = 800,
        chunk_overlap = 150
    )

    chunks = splitter.split_text(text)

    return chunks