# Upwork API RAG Support Bot

Grounded RAG-based technical support assistant for answering Upwork API queries using LangChain, FAISS, Streamlit, and Llama 3.1.

---

# Overview

This project is a production-style Retrieval-Augmented Generation (RAG) system built for answering technical questions related to the Upwork API documentation.

The application ingests Upwork API technical reference documents, converts them into semantic embeddings, stores them in a vector database, and retrieves the most relevant documentation chunks during user queries.

The system is designed with:
- Semantic Retrieval
- Hallucination Prevention
- Prompt Injection Defense
- Grounded Responses
- Source Transparency
- Latency Tracking

---

# Architecture

```text
User Query
      ↓
Query Guardrails
      ↓
Semantic Retrieval (FAISS)
      ↓
Top Relevant Chunks
      ↓
Grounded Prompt
      ↓
Llama 3.1 (DeepInfra)
      ↓
Answer + Sources + Latency
```

---

# Features

-  PDF-based documentation ingestion
-  Semantic search using vector embeddings
-  Retrieval-Augmented Generation (RAG)
-  Prompt injection protection
-  Hallucination guardrails
-  Source transparency
-  API latency tracking
-  Deterministic grounded responses
-  Persistent ChromaDB vector storage
-  Interactive Streamlit UI

---

# Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| Framework | LangChain |
| Vector Database | FAISS |
| Embedding Model | sentence-transformers/all-MiniLM-L6-v2 |
| LLM | Llama 3.1 via DeepInfra |
| UI | Streamlit |
| PDF Parsing | PyPDF |
| Environment Management | python-dotenv |

---

# Project Structure

```text
upwork-api-rag-support-bot/
│
├── app.py
├── ingest.py
├── rag_pipeline.py
├── requirements.txt
├── .env.example
├── README.md
│
├── data/
│   └── upwork_api_docs.pdf
│
└── utils/
    └── prompts.py
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/sidhanth01/upwork-api-rag-support-bot.git
cd upwork-api-rag-support-bot
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file:

```env
DEEPINFRA_API_KEY=your_api_key_here
```

---

# Data Ingestion

Run the ingestion pipeline to:
- Load the PDF
- Chunk the documentation
- Generate embeddings
- Store vectors in FAISS

```bash
python ingest.py
```

---

# Run Application

```bash
streamlit run app.py
```

---

# Sample Questions

## Question 1

```text
What is the specific request-per-second rate limit for the Upwork API, and is it enforced per Key or per IP?
```

---

## Question 2

```text
How long is an OAuth access token valid for?
```

---

## Question 3

```text
Can I use a Client Credentials Grant to access a user's private contract details?
```

---

# Guardrails & Safety

The system includes multiple safety mechanisms:

- Prompt injection defense
- Hallucination prevention
- Grounded-only answering
- Deterministic responses
- Strict context-based generation

If the answer is not present in the retrieved documentation, the model responds with:

```text
I'm sorry, but the provided documentation does not contain that information.
```

---

# Retrieval Strategy

The system uses:
- RecursiveCharacterTextSplitter
- Chunk size: 500
- Chunk overlap: 50
- Semantic retrieval with FAISS
- Top-3 relevant chunk retrieval

Chunk overlap is important because technical documentation and code snippets often span multiple chunk boundaries. Overlap helps preserve semantic continuity and improves retrieval quality.

---

# Source Transparency

The UI displays:
- Generated Answer
- Retrieved Documentation Sources
- API Response Latency

This improves:
- explainability
- trustworthiness
- grounding visibility

---

# Latency Tracking

The application measures and displays:
- end-to-end LLM response latency
- retrieval + generation timing

---

# Production-Oriented Improvements

Implemented:
- Modular architecture
- Persistent vector database
- Prompt injection protection
- Grounded prompting
- Semantic retrieval
- Deterministic generation

Potential future improvements:
- Hybrid Retrieval (BM25 + Vector Search)
- Reranking Models
- Redis Caching
- Streaming Responses
- Evaluation Pipelines
- Observability & Monitoring

---

# Challenges Faced

- Preventing hallucinated API responses
- Maintaining retrieval grounding
- Balancing retrieval quality and concise responses

---

# How LLMs Assisted Development

LLMs were used for:
- debugging assistance
- prompt engineering iterations
- retrieval strategy refinement
- Streamlit UI improvements
- architecture validation

No proprietary Upwork documentation was uploaded to public models.

---

# Why I Am a Strong Fit for the ProAnalyst AI Team

- Strong understanding of RAG systems and vector retrieval
- Focus on production-oriented AI system design
- Experience building grounded and reliable LLM applications

---

# License

This project is developed for educational and assessment purposes.

---

# 👨‍💻 Author

Sidhanth L

AI/ML Engineer | Generative AI | RAG Systems | LLM Applications
