from langchain_chroma import Chroma
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
embd_key = os.getenv("EMBEDDING_KEY")
DB_DIR = "./backend/chroma_db"

def build_vector_store(chunking_list: list, embd_model: str):
    """
        Cria os chunks como vetores dentro do banco
    """

    try:
        embd = FastEmbedEmbeddings(model_name = embd_model)

        return Chroma.from_documents(documents=chunking_list,
                                        embedding=embd,
                                        persist_directory=DB_DIR)
    except Exception as e:
        raise RuntimeError("Falha na inicialização do banco ", e)

def load_vector_store(embd_model: str):
    """
        Carrega o banco vetorial já criado para consultas vindas do chatbot.
    """

    try:
        embd = FastEmbedEmbeddings(model_name= embd_model)

        return Chroma(persist_directory=DB_DIR,
                      embedding_function=embd)
    
    except Exception as e:
        raise RuntimeError("Falha no carregamento do banco ", e)
