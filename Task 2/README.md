# Simple RAG System (Retrieval-Augmented Generation)

This project is a **simple RAG (Retrieval-Augmented Generation) system** that lets you ask any question and get an answer based on the data stored in `docs.json`.  
It uses **FAISS** for vector search, **Sentence Transformers** for embeddings, and an **LLM API** for generating concise paraphrased answers.

---

## Features
- Interactive **Streamlit** web app.
- Document retrieval using **FAISS**.
- Embeddings generated with **SentenceTransformer (all-MiniLM-L6-v2)**.
- LLM-based response generation with concise paraphrasing.
- Displays:
- Final LLM reply (paraphrased).
- Original answer from database.
- Context sent to the LLM.
- Top database matches.

---

## Project Structure
```bash
├── app.py # Main Streamlit app
├── vector_store.py # VectorStore (FAISS logic)
├── embeddings.py # Embedding function
├── llm_client.py # LLM API client & answer generator
├── docs.json # Knowledge base (Q&A pairs)
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

---

## ⚙️ Installation

1. **Clone** the repository:
   ```bash
   git clone https://github.com/mohamedelawakey/ghaymah.git
   cd repo
   ```
   
--- 

## Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

---

## Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔑 Environment Variables
Create a .env file in the project root and add your API key:
   ```bash
   OPENAI_API_KEY=your_api_key_here
   ```

---

## ▶️ Usage

Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
Open the app in your browser:
   ```bash
   http://localhost:8501
   ```
Type your question in the input box, and you’ll see:
- A concise LLM-generated reply.
- The original database answer.
- The context sent to the LLM.
- Top database matches.

---

## 📦 Requirements

All dependencies are listed in requirements.txt:
- faiss_cpu==1.12.0
- numpy==2.3.2
- openai==1.107.0
- python-dotenv==1.1.1
- sentence_transformers==5.1.0
- streamlit==1.48.1

---