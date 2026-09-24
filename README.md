# 🤖 RAG Document Assistant

> **An AI-powered document question-answering system using Retrieval-Augmented Generation (RAG), LangChain, ChromaDB, Hugging Face embeddings, Gemini, and Streamlit.**

Ask questions about your PDF documents and get **context-aware answers based on the uploaded content** — instead of relying only on the LLM's general knowledge.

---

## ✨ Features

* 📄 **PDF Document Upload** — Upload your own PDF documents.
* 🔍 **Semantic Search** — Finds the most relevant sections of your documents.
* 🧠 **Retrieval-Augmented Generation** — Combines document retrieval with an LLM to generate answers.
* 💬 **Natural Language Q&A** — Ask questions in a conversational way.
* ⚡ **Vector Search** — Uses ChromaDB for efficient similarity-based retrieval.
* 🔤 **Text Embeddings** — Converts document chunks into vector representations using Hugging Face embeddings.
* 🤖 **Gemini LLM** — Generates answers using the retrieved document context.
* 🖥️ **Streamlit Interface** — Simple and interactive web-based UI.

---

## 🧩 How It Works

The application follows a complete RAG pipeline:

```text
            📄 PDF Document
                  │
                  ▼
          ┌─────────────────┐
          │  Text Extraction │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │  Text Chunking   │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │    Embeddings    │
          │ Hugging Face     │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │    ChromaDB      │
          │  Vector Store    │
          └────────┬────────┘
                   │
             User Question
                   │
                   ▼
          ┌─────────────────┐
          │ Similarity Search│
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │ Relevant Context │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │   Gemini LLM     │
          └────────┬────────┘
                   │
                   ▼
             💬 AI Answer
```

---

## 🛠️ Tech Stack

| Technology           | Purpose                                 |
| -------------------- | --------------------------------------- |
| 🐍 **Python**        | Core programming language               |
| 🦜 **LangChain**     | RAG pipeline and LLM integration        |
| 🗄️ **ChromaDB**     | Vector database for document embeddings |
| 🤗 **Hugging Face**  | Text embedding generation               |
| ✨ **Google Gemini**  | Large Language Model                    |
| 📄 **PyPDF**         | PDF text extraction                     |
| 🌐 **Streamlit**     | Web application interface               |
| 🔐 **python-dotenv** | Environment variable management         |

---

## 📂 Project Structure

```text
RAG-Document-Assistant/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── chroma_db/
│   └── vector_store/
│
└── documents/
    └── sample.pdf
```

> **Note:** API keys and sensitive environment variables should never be committed to GitHub.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Navigate to the Project

```bash
cd RAG-Document-Assistant
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
HF_TOKEN=your_huggingface_token
```

Replace the values with your own API credentials.

**Never upload your `.env` file to GitHub.**

Add this to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
chroma_db/
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💬 Example Workflow

### Step 1 — Upload a PDF

Upload a document such as:

```text
📄 Machine Learning Notes.pdf
```

### Step 2 — Document Processing

The application:

1. Extracts text from the PDF
2. Splits the text into smaller chunks
3. Generates embeddings
4. Stores the embeddings in ChromaDB

### Step 3 — Ask a Question

For example:

```text
What is supervised learning?
```

### Step 4 — Retrieval

The system searches the vector database and retrieves the most relevant document chunks.

### Step 5 — Generation

The retrieved context is provided to Gemini, which generates a natural-language answer.

---

## 🧠 RAG Pipeline

The core concept behind this project is **Retrieval-Augmented Generation**.

Instead of directly sending a question to an LLM:

```text
Question → LLM → Answer
```

this project uses:

```text
Question
   ↓
Vector Search
   ↓
Relevant Document Chunks
   ↓
Context + Question
   ↓
Gemini
   ↓
Grounded Answer
```

This allows the application to answer questions using information contained in the user's documents.

---

## 🔍 Chunking & Embeddings

Documents are divided into smaller chunks before generating embeddings.

Example configuration:

```text
Chunk Size: 500
Chunk Overlap: 50
```

Each chunk is converted into a numerical vector representation using a Hugging Face embedding model.

These vectors are then stored in **ChromaDB**.

When the user asks a question, the question is also converted into an embedding and compared against the stored vectors to find semantically similar content.

---

## 📊 Why ChromaDB?

ChromaDB is used as the vector store because it provides an easy way to:

* Store document embeddings
* Perform similarity searches
* Retrieve relevant document chunks
* Integrate with LangChain

---

## 🚀 Future Improvements

Some possible improvements for future versions:

* [ ] Support multiple document formats
* [ ] Multi-PDF conversations
* [ ] Chat history and memory
* [ ] Source citations for generated answers
* [ ] Document preview
* [ ] Improved chunking strategies
* [ ] Metadata filtering
* [ ] Authentication
* [ ] Cloud vector database
* [ ] Streaming responses
* [ ] Better hallucination detection
* [ ] Deployment with production-grade infrastructure

---

## 📸 Screenshots

Add screenshots of the application here:

```text
screenshots/
├── home.png
├── upload.png
└── chat.png
```

Example:

![RAG Document Assistant](screenshots/home.png)

---

## 🌐 Live Demo

🚀 **Streamlit App:**
`YOUR_STREAMLIT_APP_URL`

---

## 📌 Project Highlights

* Built a complete **Retrieval-Augmented Generation pipeline**
* Implemented **semantic document retrieval**
* Used **vector embeddings and similarity search**
* Integrated **Google Gemini LLM**
* Built an interactive **Streamlit application**
* Worked with **LangChain and ChromaDB**
* Implemented environment-based API key management

---

## 👨‍💻 Author

### Sheikh Faheem Ahmed

**AI & ML Engineering | Python | Generative AI | RAG | Flutter**

🔗 GitHub:
`https://github.com/sheikh-faheem`

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub!

---

### 📜 License

This project is created for educational and portfolio purposes.
