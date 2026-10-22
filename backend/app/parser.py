from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders import CSVLoader
import re

def parse_document(path:str , mode:str) -> list[str]:

    loaders = {
        "pdf": PyPDFLoader,
        "docs": Docx2txtLoader,
        "csv": CSVLoader,
    }

    if mode not in loaders:
        raise ValueError(f"Modo {mode} Inválido: Escolha entre pdf, docs, csv")
    
    try:
        documents = loaders[mode](path).load()

        for doc in documents:
            doc.page_content = re.sub(r'\s+', ' ', doc.page_content).strip()

        return documents

    except Exception as e: 
        raise RuntimeError(f"Erro: {e}")
