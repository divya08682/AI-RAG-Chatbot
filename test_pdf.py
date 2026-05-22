from src.pdf_loader import load_pdf
from src.text_chunker import split_text
from src.embeddings import get_embeddings
from src.vector_store import create_vector_store

docs = load_pdf("sample.pdf")

chunks = split_text(docs)

embeddings = get_embeddings()

vector_db = create_vector_store(
    chunks,
    embeddings
)

print("Vector DB Created Successfully")