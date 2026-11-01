from parser import parse_document
from chunking import chunking
from vector_store import build_vector_store, load_vector_store

def ingestion_flow(doc_path: str, doc_mode: str, embd_model: str):

    text = parse_document(path=doc_path, mode=doc_mode)
    splitter = chunking(text)
    build_vector_store(splitter, embd_model)


def get_retriever(embd_model: str, k: int = 4):
    vector_db = load_vector_store(embd_model)
    return vector_db.as_retriever(search_type='similarity',
                                  search_kwargs={"k": k})

