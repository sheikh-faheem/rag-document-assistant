import os
import tempfile

import streamlit as st
from dotenv import load_dotenv
from google import genai

from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# -----------------------------------
# Configuration
# -----------------------------------

load_dotenv()

st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="📚",
    layout="centered"
)


# -----------------------------------
# Gemini
# -----------------------------------

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API key is not configured.")
    st.stop()

client = genai.Client(api_key=api_key)


# -----------------------------------
# Embedding model
# -----------------------------------

@st.cache_resource
def load_embeddings():

    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


embeddings = load_embeddings()


# -----------------------------------
# UI
# -----------------------------------

st.title("📚 AI Document Assistant")

st.write(
    "Upload a PDF and ask questions about its contents."
)


uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)


# -----------------------------------
# Process PDF
# -----------------------------------

if uploaded_file:

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )

    if st.button("Process Document"):

        with st.spinner(
            "Reading and processing your document..."
        ):

            # Save uploaded PDF temporarily
            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".pdf"
            ) as temp_file:

                temp_file.write(
                    uploaded_file.getvalue()
                )

                pdf_path = temp_file.name


            # Read PDF
            reader = PdfReader(pdf_path)

            text = ""

            for page in reader.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text


            # Split text
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=500,
                chunk_overlap=50
            )

            chunks = text_splitter.split_text(text)


            # Create unique database directory
            db_path = "./chroma_db"


            # Create ChromaDB
            vectorstore = Chroma.from_texts(
                texts=chunks,
                embedding=embeddings,
                persist_directory=db_path,
                collection_name="documents"
            )


            # Store in session
            st.session_state.vectorstore = vectorstore
            st.session_state.document_processed = True


            st.success(
                f"Document processed successfully! "
                f"Created {len(chunks)} chunks."
            )


# -----------------------------------
# Question answering
# -----------------------------------

if st.session_state.get(
    "document_processed",
    False
):

    st.divider()

    st.subheader("💬 Ask your document")

    question = st.text_input(
        "Enter your question:"
    )


    if st.button("Ask AI"):

        if not question:

            st.warning(
                "Please enter a question."
            )

            st.stop()


        # Retrieve relevant chunks
        results = st.session_state.vectorstore.similarity_search(
            question,
            k=3
        )


        # Combine context
        context = "\n\n".join(
            result.page_content
            for result in results
        )


        # RAG prompt
        prompt = f"""
You are a helpful document assistant.

Answer the question using ONLY the
information contained in the context below.

If the answer cannot be found in the context,
say:

"I couldn't find that information in the document."

Context:

{context}

Question:

{question}

Answer:
"""


        # Gemini
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )


        # Display answer
        st.subheader("🤖 Answer")

        st.write(response.text)


        # Display sources
        with st.expander(
            "📄 View retrieved information"
        ):

            for i, result in enumerate(
                results,
                start=1
            ):

                st.markdown(
                    f"**Source {i}**"
                )

                st.write(
                    result.page_content
                )

                st.divider()