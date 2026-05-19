# Upwork API Technical Support Bot

A RAG-based AI assistant that answers technical questions about the Upwork API documentation.

## Features

- Retrieval-Augmented Generation (RAG)
- Semantic search using ChromaDB
- Local embeddings using MiniLM
- Grounded technical responses
- Hallucination prevention
- Streamlit web interface
- Source chunk display
- API latency tracking

## Tech Stack

- Python
- LangChain
- ChromaDB
- Streamlit
- DeepInfra Llama 3.1
- Sentence Transformers

## Setup

### Install dependencies

pip install -r requirements.txt

### Add API key

Create `.env`:

DEEPINFRA_API_KEY=your_api_key

### Add PDF

Place the Upwork API documentation PDF inside:

data/upwork_api_docs.pdf

### Run ingestion

python ingest.py

### Launch app

streamlit run app.py