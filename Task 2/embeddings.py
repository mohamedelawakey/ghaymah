from sentence_transformers import SentenceTransformer

# embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text):
    return embedding_model.encode([text])[0]