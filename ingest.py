from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

PDF_PATH = "data/upwork_api_docs.pdf"

print("\nLoading PDF...")

# Load PDF
loader = PyPDFLoader(PDF_PATH)
documents = loader.load()

# Combine all text
full_text = "\n".join([doc.page_content for doc in documents])

# SANITY CHECK
print("\n===== SANITY CHECK =====")
print(f"Total Character Count: {len(full_text)}")

print("\n===== SAMPLE TEXT =====")
print(full_text[:1000])

# Chunking
print("\nCreating chunks...")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

print(f"Total Chunks Created: {len(chunks)}")

# Embedding model
print("\nLoading embedding model...")

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Store in ChromaDB
print("\nCreating ChromaDB...")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma_db"
)

print("\nChromaDB successfully created and persisted.")