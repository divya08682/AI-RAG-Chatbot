from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def create_rag_chain(vector_db):

    llm = ChatGroq(
        model_name="llama3-8b-8192"
    )

    return llm, vector_db