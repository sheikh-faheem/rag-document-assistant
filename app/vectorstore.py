from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# -----------------------------
# 1. Load PDF
# -----------------------------

pdf_path = "data\document\Sheikh Faheem Ahmed offer letter.pdf"

reader = PdfReader(pdf_path)

text = ""

for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text


# -----------------------------
# 2. Split text into chunks
# -----------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_text(text)

print("Total chunks:", len(chunks))


# -----------------------------
# 3. Create embedding model
# -----------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# -----------------------------
# 4. Store chunks in ChromaDB
# -----------------------------

vectorstore = Chroma.from_texts(
    texts=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

print("Successfully stored documents in ChromaDB!")