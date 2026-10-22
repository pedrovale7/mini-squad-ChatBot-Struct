from langchain_text_splitters import RecursiveCharacterTextSplitter
from parser import parse_document

def chunking(documents) -> list[str]:

    splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", " ", ""],
        chunk_size = 300,
        chunk_overlap = 30
    )

    chunks = splitter.split_documents(documents)

    return chunks