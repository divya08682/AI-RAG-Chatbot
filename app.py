import streamlit as st

from src.pdf_loader import load_pdf
from src.text_chunker import split_text
from src.embeddings import get_embeddings
from src.vector_store import create_vector_store
from src.rag_pipeline import create_rag_chain

st.title("AI RAG Chatbot")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_file:

    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    docs = load_pdf(uploaded_file.name)

    chunks = split_text(docs)

    embeddings = get_embeddings()

    vector_db = create_vector_store(
        chunks,
        embeddings
    )

    llm, vector_db = create_rag_chain(
        vector_db
    )

    question = st.text_input(
        "Ask a Question"
    )

    if question:

        results = vector_db.similarity_search(
            question,
            k=2
        )

        context = "\n".join(
            [doc.page_content for doc in results]
        )

        prompt = f"""
        Answer the question based on the context below.

        Context:
        {context}

        Question:
        {question}
        """

        response = llm.invoke(prompt)

        st.write(response.content)