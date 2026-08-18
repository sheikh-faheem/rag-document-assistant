from dotenv import load_dotenv
from google import genai

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# Load environment variables
load_dotenv()


# Connect to Gemini
client = genai.Client()


# Load the same embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# Connect to our existing ChromaDB
vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)


# Ask the user
question = input("\nAsk a question about your document: ")


# Retrieve relevant chunks
results = vectorstore.similarity_search(
    question,
    k=3
)


# Combine retrieved chunks
context = "\n\n".join(
    result.page_content
    for result in results
)


# Create the RAG prompt
prompt = f"""
You are a helpful document assistant.

Answer the user's question using ONLY the information
provided in the context below.

If the answer cannot be found in the context,
say: "I couldn't find that information in the document."

Context:
{context}

Question:
{question}

Answer:
"""


# Generate answer using Gemini
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)


print("\n--- AI ANSWER ---\n")
print(response.text)