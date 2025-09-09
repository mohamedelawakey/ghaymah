import faiss
import numpy as np
import json
from embeddings import get_embedding

class VectorStore:
    def __init__(self, docs_path = "docs.json"):
        with open(docs_path, "r", encoding = "utf-8") as f:
            self.docs = json.load(f)

        self.questions = [doc["question"] for doc in self.docs]
        self.answers = [doc["answer"] for doc in self.docs]

        self.dimension = len(get_embedding(self.questions[0]))
        self.index = faiss.IndexFlatL2(self.dimension)

        embeddings = np.array([get_embedding(q) for q in self.questions])
        self.index.add(embeddings)

    def search(self, query, k = 1):
        query_emb = np.array([get_embedding(query)])
        distances, indices = self.index.search(query_emb, k)
        results = [(self.questions[i], self.answers[i]) for i in indices[0]]
        return results