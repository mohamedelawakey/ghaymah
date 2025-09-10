from gensim.models import Word2Vec
import numpy as np

embedding_model = Word2Vec(vector_size = 512,
                           window = 5,
                           min_count = 1,
                           workers = 2)

VECTOR_DIM = 512

def get_embedding(text):
    words = text.split()
    word_vecs = []

    for word in words:
        if word in embedding_model.wv:
            word_vecs.append(embedding_model.wv[word])

    if len(word_vecs) == 0:
        vec = np.zeros(VECTOR_DIM)
    else:
        vec = np.mean(word_vecs, axis=0)

    if len(vec) < VECTOR_DIM:
        vec = np.pad(vec, (0, VECTOR_DIM - len(vec)))
    elif len(vec) > VECTOR_DIM:
        vec = vec[:VECTOR_DIM]

    return vec.tolist()
