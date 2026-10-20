from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from langchain_community.document_loaders import CSVLoader
import re

def parse_document(path:str , mode:str) -> list[str]:

    loaders = {
        "pdf": PyPDFLoader,
        "docs": UnstructuredWordDocumentLoader,
        "csv": CSVLoader,
    }

    if mode not in loaders:
        raise ValueError(f"Modo {mode} Inválido: Escolha entre pdf, docs, csv")
    
    try:
        documents = loaders[mode](path).load()[0]

        doc_format= "\n".join(documents.page_content.split())
        doc_format = re.sub(r"(?<!\n)\n(?!\n)", " ", doc_format)
        doc_format = re.sub(r"[ \t]+", " ", doc_format)
        
        return doc_format

    except Exception as e: 
        raise RuntimeError(f"Erro: {e}")
