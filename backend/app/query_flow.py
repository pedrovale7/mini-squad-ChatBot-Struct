from langchain.chat_models import init_chat_model
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from ingestion_pipeline import get_retriever
from dotenv import load_dotenv




load_dotenv()

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def get_llm(provider: str = "groq", model: str = "openai/gpt-oss-20b", temperature: float = 0):
    # a chave é lida do .env (ex.: GROQ_API_KEY)
    return init_chat_model(model, model_provider=provider, temperature=temperature)

def build_chain(retriever, prompt, llm):
    return (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )


if __name__ == "__main__":
    print("iniciando teste de consulta RAG...")

    # carrega o retriever
    retriever = get_retriever(embd_model="intfloat/multilingual-e5-large")

    # instancia a LLM
    llm = get_llm()

    # prompt provisorio (parte do mateus)
    # Todo: Substituir pelo prompt oficial do Mateus
    prompt_provisorio = ChatPromptTemplate.from_template(
        #"Responda à pergunta usando apenas o seguinte contexto extraído dos documentos da empresa júnior:\n\n"
        "Responda à pergunta usando apenas o seguinte contexto extraído sobre as atividades obrigatórias:\n\n"
        "Contexto: {context}\n\n"
        "Pergunta: {question}\n\n"
        "Resposta:"
    )


    # monta a chain que conecta tudo
    chain = build_chain(retriever, prompt_provisorio, llm)

    # executa a consulta
    #pergunta_teste = "Quais são os serviços prestados pela empresa?"
    pergunta_teste = "Quais são as atividades obrigatórias?"
    print(f"\nPergunta: {pergunta_teste}\nProcessando...\n")


    try:
        resultado = chain.invoke(pergunta_teste)
        print("Resultado:")
        print(resultado)

    except Exception as e:
        print(f"Erro ao processar a chain: {e}")