## TODOs

0. Configuração Inicial:
   - Dependencias (FRAMEWORKS: Vector Storage, LLM/Embedding Provider, RAG Orchestrator)
   - ChaveAPI
   - Escolher o Escopo do Projeto.

1. Datasets e Pre-processamentos (PIPELINE 1):
   - Escolher um Dataset dentro do Escopo
   - Manipulação e Limpeza dos dados

2. Ingestion Flow (PIPELINE 2):
   - Parsing : Transformar a fonte em string.
   - Chunking/Splitting: Dividir o documento em pedaços.
   - Embeddings: Pegar esses chunks e transformar em vetores numéricos.
   - Vector Storage: Armazenar esse vetores no banco vetorial.
   - Retriever : como retornar chunks especificos (similaridade dos cossenos?)

3. Query Flow:
   - Configuração do LLM provider
   - Prompt Engineering
   - Montar a chain RAG

4. Front-end:
   - Vai ter ?

## IDEIAS DE PROJETOS

1. RAG para Documentação de API usadas na Struct
   - Escopo: Parse docs de uma API (OpenAI, Stripe, GitHub), cria RAG, serve via chatbot simples
   - Por que funciona: Documentação bem estruturada = chunks perfeitos
   - Portfólio: "Chatbot que responde perguntas sobre APIs"
   - Tempo: 2-3 semanas
   - Stack: LangChain + Pinecone + FastAPI + React simples

2. RAG para o FAQ da Struct
   - Escopo: Alimenta conhecimento da Struct (processos, regras, histórico) num chatbot
   - Por que funciona: Dados já existem, problema real
   - Portfólio: Case de uso interno + screenshot do bot funcionando
   - Tempo: 2 semanas
   - Bônus: A Empresa usa, você ganha credibilidade

3. RAG para Livros/Papers Acadêmicos
   - Escopo: Upload PDF, cria RAG, chatbot responde perguntas sobre o conteúdo
   - Por que funciona: Interface simples, problema bem definido
   - Portfólio: "Document Q&A system"
   - Tempo: 1-2 semanas
   - Upgrade futuro: Suportar múltiplos PDFs

4. Chatbot de Análise de Código (GitHub RAG)
   - Escopo: Clona repo GitHub, indexa código, chatbot responde "onde tá essa função?" ou "como funciona?"
   - Por que funciona: Devs querem explorar código rápido
   - Portfólio: Muito técnico, impressiona
   - Tempo: 2-3 semanas
   - Desafio: Lidar com sintaxe de múltiplas linguagens

5. RAG para toda a Base de Conhecimento da EJ
   - Escopo: FAQs + docs + planilhas da EJ → RAG
   - Por que funciona: Você coleta dados reais de qualidade
   - Portfólio: "RAG system com metrics de performance"
   - Tempo: 3 semanas (1 semana extra para feedback loop)
