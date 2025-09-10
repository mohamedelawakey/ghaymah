# llm_client.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key  = api_key,
                base_url="https://genai.ghaymah.systems"
)

SYSTEM_PROMPT = (
    "You are a concise assistant.\n"
    "Answer ONLY using the provided context.\n"
    "Write in the SAME language as the question.\n"
    "Paraphrase the answer briefly (1–2 sentences). Do NOT copy verbatim.\n"
    "If the context is insufficient, reply exactly: Not found in knowledge base."
)

def generate_answer(query, context):
    prompt = (
        "Use ONLY the following context.\n"
        "Context:\n-----\n"
        f"{context}\n"
        "-----\n"
        f"Question: {query}\n"
        "Final concise answer (paraphrased):"
    )

    response = client.chat.completions.create(
        model = "DeepSeek-V3-0324",
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        max_tokens = 150,
        temperature = 0.2
    )
    return response.choices[0].message.content.strip()
