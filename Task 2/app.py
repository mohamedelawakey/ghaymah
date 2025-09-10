import streamlit as st
from llm_client import generate_answer
from ghaymah_vector_store import VectorStore

# ======== Serverless Vector Store URL ========
HOST = "https://serverless-store-77838979b96f.hosted.ghaymah.systems"

# Initialize VectorStore
store = VectorStore(HOST)

st.title("Simple RAG System (Serverless Version)")
st.write("Ask any question and you'll get an answer from Ghaymah Docs Knowledge Base")

query = st.text_input("Write your question here:")

if query:
    try:
        results = store.search(query, k = 5)

        if not results:
            st.warning("No results found in docs.")
        else:
            context = "\n\n".join([f"Q: {q}\nA: {a}" for q, a in results if q and a])
            raw_db_top1 = results[0][1]

            answer = generate_answer(query, context)

            st.subheader("LLM Reply (from Docs)")
            st.write(answer)

            with st.expander("Raw DB Top 1 (for comparison)"):

                st.write(raw_db_top1)

            with st.expander("Context sent to LLM"):
                st.code(context)

            with st.expander("Top matches from vector DB"):
                st.write(results)
    except Exception as e:
        st.error(f"Error: {e}")
