import os
import time

from dotenv import load_dotenv
from openai import OpenAI

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from utils.prompts import SYSTEM_PROMPT

# Load environment variables
load_dotenv()

# DeepInfra Client
client = OpenAI(
    api_key=os.getenv("DEEPINFRA_API_KEY"),
    base_url="https://api.deepinfra.com/v1/openai"
)

# Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load persistent ChromaDB
vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)


# -----------------------------
# Guardrail Layer
# -----------------------------
def is_malicious_query(query: str) -> bool:

    blocked_patterns = [
        "ignore previous instructions",
        "ignore system prompt",
        "reveal system prompt",
        "show hidden prompt",
        "developer instructions",
        "forget your instructions",
        "bypass restrictions",
        "jailbreak",
        "act as",
        "pretend to be",
        "override safety",
        "disable guardrails"
    ]

    query_lower = query.lower()

    return any(pattern in query_lower for pattern in blocked_patterns)


# -----------------------------
# Main RAG Pipeline
# -----------------------------
def ask_question(user_query):

    # -----------------------------
    # Query Guardrails
    # -----------------------------
    if is_malicious_query(user_query):

        return (
            "Prompt injection attempt detected. Request rejected.",
            [],
            0
        )

    # -----------------------------
    # Semantic Retrieval
    # Using MMR for diverse chunks
    # -----------------------------
    retrieved_docs = vectorstore.max_marginal_relevance_search(
        user_query,
        k=3,
        fetch_k=10
    )

    # Combine retrieved chunks
    context = "\n\n---\n\n".join([
    doc.page_content for doc in retrieved_docs
])

    # Final grounded prompt
    final_prompt = f"""
Retrieved Documentation Context:
{context}

Developer Question:
{user_query}

Provide a grounded technical answer using ONLY the retrieved documentation.
"""

    # -----------------------------
    # Measure API Latency
    # -----------------------------
    start_time = time.time()

    # -----------------------------
    # LLM API Call
    # -----------------------------
    response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        temperature=0,
        top_p=0.9,
        max_tokens=300,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": final_prompt
            }
        ]
    )

    end_time = time.time()

    latency = round(end_time - start_time, 2)

    # -----------------------------
    # Extract Final Answer
    # -----------------------------
    answer = response.choices[0].message.content.strip()
    # Hide weak sources for fallback responses
    if "does not contain that information" in answer.lower():
        sources = []

    # -----------------------------
    # Extract Source Chunks
    # -----------------------------
    sources = []

    for idx, doc in enumerate(retrieved_docs[:3], start=1):

        source_text = {
            "source_number": idx,
            "content": doc.page_content
        }

        sources.append(source_text)

    return answer, sources, latency