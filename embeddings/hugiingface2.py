from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Query
query = "delivery job kya hoti hai"

# Documents
documents = [
    "fleet executive road pe delivery karta hai",  # similar hona chahiye
    "software engineer code likhta hai",           # alag
    "data scientist ML models banata hai"          # alag
]

# Embed karo
query_vector = embeddings.embed_query(query)
doc_vectors = embeddings.embed_documents(documents)

# Similarity calculate karo
query_arr = np.array(query_vector).reshape(1, -1)
doc_arr = np.array(doc_vectors)

similarities = cosine_similarity(query_arr, doc_arr)[0]

print("Query:", query)
print("\n--- Similarity Scores ---")
for i, (doc, score) in enumerate(zip(documents, similarities)):
    print(f"\nDoc {i+1}: {doc}")
    print(f"Score: {score:.4f}")