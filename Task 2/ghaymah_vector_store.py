import requests
from embeddings import get_embedding

class VectorStore:
    def __init__(self, host_url):
        self.host = host_url

    def search(self, query, k=3):

        vector = get_embedding(query)
        payload = {"vector": vector, "k": k}

        response = requests.post(
            f"{self.host}/search",
            json=payload,
            headers={"Content-Type": "application/json"}
        )

        if response.status_code != 200:
            raise Exception(f"Search failed: {response.text}")

        data = response.json()
        print("DEBUG: response JSON:", data)

        results_list = data.get("results") or data.get("data") or []
        return [(r["payload"].get("question", ""), r["payload"].get("answer", "")) for r in results_list]
