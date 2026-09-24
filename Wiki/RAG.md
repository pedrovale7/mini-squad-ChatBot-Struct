## Ideia Inicial : Construir um Chatbot focado em Documentações Técnicas

- Chat bot com arquitetura RAG para documentos
  - Benefícios de usar o RAG: (Precisão elevada, Flexibilidade sobre adições de novos documentos e Escalabilidade)

## RAG - Teórico

### Como construir uma aplicação RAG

Tudo começa com um bom problema que você quer resolver!

Componentes Essenciais:

- Modelo de Embedding: representa textos por vetores. Usaremos embedding tanto no banco de documentos quanto na query do usuário.

- Banco de Dados Vetorial: Depois do modelo de embeddings, precisamos guardar todos os dados em um banco vetorial para conseguir buscar esses vetores.

- LLM: Gera as respostas baseado nos documentos recuperados que tem contexto com o input do usuário.

Workflow:

1. Ingestão dos dados

- Dividir (split) os documentos em pequenos pedaços (chunks).

- Gerar embeddings para cada chunk.

- Armazena-los em um vector db.

2. Processamento do input

- Converter a query do usuário em embedding.

- Buscar no vector db por semelhanças de vetores em relação a query e os documentos. Quais documentos tem maior contexto com a pergunta inicial? Mas como foi dividido, ent pegará os pedaços de documentos mais semelhantes.

- Recuperar os melhores chunks e o input e mandarem juntos para uma LLM geradora.

### Frameworks

Vector Storage:

- Chroma

- FAISS

- Pinecone

LLM/Embeddings

- OpenAI

- Transformers

- Sentence Transformers

- google genai

Orquestrador RAG

- LangChain

- LangGraph

- LlamaIndex

### Ingestion Flow

Fases:

- Reconhecimento da Fonte de dados

- Parsing

- Chunking ou Spliting

- Embedding

- Vector Store

#### Parsing

Sabemos que as LLMs recebem inputs em NLP, em formatos de textos. Então, nos precisamos "tratar" os dados da fonte até conseguir dados textuais (strings). Ou seja, se sua fonte de dados for uma dúzia de PDF, você deve usar algum leitor de PDF e retornar os textos dele.

- Biblioteca:
  - pypdf: PDF

  - python-docx: DOCS

  - beautifulsoup: HTML

#### Chunking

- Consiste em dividir strings em pedaços menores, por exemplo, dividir um artigo grande em parágrafos ou seções.

- Porque Chuncking ?
  - Fazemos esse spliting pois a janela de contexto de um modelo de embedding é pequeno. Então, essa prática ajuda em maximizar a janela de contexto, relevante para criar uma vetorização dos tokens.

  - Torna mais específico, pois textos grandes podem abordar muitos tópicos.

  - Limite de Tokens do LLM gerador

#### Embedding

- Consiste em transformar os chunks em vetores que capturam sentido semântico nas palavras

#### Vector Store e Retriever

- Guardar todos os dados do embedding em um banco vetorial.

- Busca por similaridade de cossenos e agrupando em k documentos mais parecidos, nesse caso é um algoritmo de KNN

### Query Processing Flow

#### Embedding no Input

- Novamente, o modelo llm exige que passamos números para ela, e também para associar vizinhos próximos com a query, tem que esta no mesmo formato que os dados.

#### Gerar o prompt na LLM

- Associando o contexto direto do banco de vetores e o input do usuário, a llm consegue usar o contexto dos documentos e responder de acordo com o contexto da pergunta.

- Faça um prompt engineer.
