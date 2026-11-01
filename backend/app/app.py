import argparse
import os
from pathlib import Path
from dotenv import load_dotenv

from ingestion_pipeline import ingestion_flow, get_retriever
from prompt import build_prompt
from query_flow import get_llm, build_chain

load_dotenv()

# TROQUE ESSAS VARIAVEIS PARA OS MODELOS QUE VOCÊ FOR USAR
EMBD_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
LLM_MODEL = "openai/gpt-oss-20b"
MODES = {".pdf": "pdf", ".docx": "docs", ".csv": "csv"}

def ingest(paths: list[str]) -> None:
    for path in paths:
        mode = MODES.get(Path(path).suffix.lower())

        if mode is None:
            print(f"Formato não suportado: {path}")
            continue

        n = ingestion_flow(path, mode, EMBD_MODEL)
        print(f"{path}: {n} chunks indexados")

def chat() -> None:
    api_key = os.getenv("GROQ_API_KEY") or os.getenv("API_KEY")
    retriever = get_retriever(EMBD_MODEL)
    chain = build_chain(retriever, build_prompt(), get_llm("groq", LLM_MODEL, api_key))

    while True:
        question = input("\nPergunta (ou 'sair'): ").strip()
        if question.lower() in {"sair", "exit"}:
            break
        if question:
            print(chain.invoke(question))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_ingest = sub.add_parser("ingest", help="indexa documentos")
    p_ingest.add_argument("paths", nargs="+")
    sub.add_parser("chat", help="inicia o chatbot")

    args = parser.parse_args()
    ingest(args.paths) if args.cmd == "ingest" else chat()