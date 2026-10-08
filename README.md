# mini-squad-ChatBot-Struct

Integrantes:
Pedro Vale - Tech Lead \\

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
pip install -r requirements.txt

# Ou com uv (se instalou uv)
uv pip install -r requirements.txt
```

⏳ **Vai levar 1-3 minutos**

---

### 4. Configurar a Chave da API

- Crie um arquivo .env igual ao .env.example

```bash
## Windows:
copy .env.example .env
## Linux:
cp .env.example .env
```

- Configure sua chave :

```python
# Mude isto:
OPENAI_API_KEY=sua-chave-api
```

### Rotina Diária

**Toda vez que abrir seu projeto:**

```bash
# 1. Ativar ambiente
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# 2. Baixar as novas dependências
pip install -r requirements.txt
uv pip install -r requirements.txt # Quem for usar o uv

```

---
