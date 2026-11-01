# mini-squad-ChatBot-Struct

## Integrantes:

- Pedro Vale - Tech Lead
- Gabriel de Castro
- Rafael Schetinger
- Henrique Gomes

## Tema : Chatbot focado em Documentações Técnicas das Diretorias

- Chat bot com arquitetura RAG para documentos (.doc, .pdf, .csv, ...);
- Escopo: FAQs + docs + planilhas da EJ;
- Benefícios de usar o RAG:
  (Precisão elevada, Flexibilidade sobre adições de novos documentos e Escalabilidade);
- Como funciona: A LLM vai estudar os documentos da EJ e com isso responder perguntas técnicas;
- Tempo Estimado: 3 semanas (1 semana extra para feedback loop);

## Como rodar o projeto:

### 1. Clonar o Repositório

```bash
# Clone o projeto
git clone <url>
```

### 2. Criar Ambiente Virtual

#### **Opção A: `.venv` Padrão (Recomendado para equipe)**

```bash
# Criar ambiente
python -m venv venv

# Ativar (escolha seu SO):

# 🐧 Linux/macOS:
source venv/bin/activate

# 🪟 Windows (CMD):
venv\Scripts\activate

# 🪟 Windows (PowerShell):
.\venv\Scripts\Activate.ps1
```

✅ **Seu terminal agora terá `(venv)` no início**

---

#### **Opção B: `uv` Rápido (Se tem 1 min para instalar uv)**

```bash
# Instalar uv (one-liner)
curl -LsSf https://astral.sh/uv/install.sh | sh  # Linux/macOS
# ou no PowerShell:
powershell -Command "irm https://astral.sh/uv/install.ps1 | iex"

# Criar ambiente
uv venv

# Ativar (mesmo processo acima)
source .venv/bin/activate  # Linux/macOS
.\venv\Scripts\Activate.ps1  # Windows PowerShell
```

---

### 3. Instalar Dependências

**Certifique-se que `(venv)` está visível no seu terminal!**

```bash
# Versão rápida (recomendada)
pip install -r backend/requirements.txt

# Ou com uv (se instalou uv)
uv pip install -r backend/requirements.txt
```

⏳ **Vai levar 1-3 minutos**

---

### 4. Configurar a chave da API

- Crie o arquivo `backend/.env` e informe a chave da Groq:

```bash
API_KEY=sua-chave-api
```

### 5. Indexar os documentos

- Adicione seus documentos em /data.
- Execute este passo uma vez inicialmente e novamente sempre que adicionar documentos novos. Os formatos suportados são `.pdf`, `.docx` e `.csv`.

```bash
python backend/app/app.py ingest ./backend/data/doc1.docx ./backend/data/doc2.pdf
```

### 6. Iniciar o chatbot

Após indexar os documentos, inicie o chat:

```bash
python backend/app/app.py chat
```

Para encerrar o chat, digite `sair`.

---
