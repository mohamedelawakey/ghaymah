import streamlit as st
from vector_store import VectorStore
from llm_client import generate_answer

store = VectorStore("docs.json")

st.title("Simple RAG System")
st.write("Ask any question and you'll get an answer based on the data in docs.json")

query = st.text_input("Write your question here:")

if query:
    results = store.search(query, k = 3)
    if not results:
        st.warning("No results found.")
    else:
        context = "\n\n".join([f"Q: {question}\nA: {answer}" for (question, answer) in results])
        raw_db_top1 = results[0][1]

        answer = generate_answer(query, context)

        st.subheader("LLM Reply (paraphrased from DB)")
        st.write(answer)

        with st.expander("Raw DB Top 1 (for comparison)"):
            st.write(raw_db_top1)

        with st.expander("Context sent to LLM"):
            st.code(context)

        with st.expander("Top matches from vector DB"):
            st.write(results)