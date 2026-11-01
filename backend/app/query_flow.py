from langchain.chat_models import init_chat_model
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def get_llm(provider: str, model: str, temperature: float = 0):
    # a chave é lida do .env (ex.: GROQ_API_KEY)
    return init_chat_model(model, model_provider=provider, temperature=temperature)

def build_chain(retriever, prompt, llm):
    return (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
