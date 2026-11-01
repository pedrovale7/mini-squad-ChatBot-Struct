## TEMA:

RAG para a Base de Conhecimento (Treinamento de Vendas) da EJ

- Escopo: docs → RAG
- Por que funciona: Você coleta dados reais e treina os modelos para entregar mais contexto
- Portfólio: "Chat Bot de Treinamento"
- Tempo: 3 semanas

## TODOs

1. Datasets e Pre-processamentos (PIPELINE 1):

- [FEITO] Manipulação e Limpeza dos dados

2. Ingestion Flow (PIPELINE 2):
   - [FEITO] Parsing : Transformar a fonte em string.
   - [FEITO] Chunking/Splitting: Dividir o documento em pedaços.
   - [FEITO] Embeddings: Pegar esses chunks e transformar em vetores numéricos.
   - [FEITO] Vector Storage: Armazenar esse vetores no banco vetorial.
   - [FEITO] Retriever : como retornar chunks especificos (similaridade dos cossenos?)

3. Query Flow:
   - [FEITO] Configuração do LLM provider (CADA UM PRECISA FAZER O SEU)
   - Prompt Engineering
   - [FEITO] Montar a chain RAG

## Possiveis Alterações no Futuro

- Automatizar limpeza dos documentos
- Armazenar os dados no formato markdown (pq é uma linguagem de marcação estrutural) que vai ajudar na performance e contexto.
- Fazer um algoritmo que evite duplicatas no banco vetorial
