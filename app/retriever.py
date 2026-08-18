from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# 1. Load the same embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# 2. Connect to our existing ChromaDB
vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)


# 3. Ask a question
question = input("\nAsk a question about your document: ")


# 4. Search for the most relevant chunks
results = vectorstore.similarity_search(
    question,
    k=3
)


# 5. Display the results
print("\n--- RELEVANT INFORMATION ---\n")

for i, result in enumerate(results, start=1):
    print(f"Result {i}:")
    print(result.page_content)
    print("\n" + "-" * 60)