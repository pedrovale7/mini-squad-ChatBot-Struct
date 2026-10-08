## TODOs

0. Configuração Inicial:
   - Dependencias (FRAMEWORKS: Vector Storage, LLM/Embedding Provider, RAG Orchestrator)

1. Datasets e Pre-processamentos (PIPELINE 1):
   - Escolher os documentos e de qual diretoria.
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

## TEMA:

5. RAG para toda a Base de Conhecimento da EJ
   - Escopo: FAQs + docs + planilhas da EJ → RAG
   - Por que funciona: Você coleta dados reais de qualidade
   - Portfólio: "RAG system com metrics de performance"
   - Tempo: 3 semanas (1 semana extra para feedback loop)
