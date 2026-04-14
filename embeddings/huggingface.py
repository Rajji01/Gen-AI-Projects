from langchain_huggingface import HuggingFaceEmbeddings

# Model load karo (first time internet se download hoga)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# ✅ Single query embed karo
vector = embeddings.embed_query("Swiggy delivery partner ki job kya hoti hai?")
print(f"Vector size: {len(vector)}")      # 384 aayega
print(f"First 5 values: {vector[:5]}")    # floats aayenge

# ✅ Multiple documents embed karo
documents = [
    "fleet executive road pe delivery karta hai",
    "software engineer code likhta hai", 
    "data scientist ML models banata hai"
]
doc_vectors = embeddings.embed_documents(documents)
print(f"\nTotal docs embedded: {len(doc_vectors)}")
print(f"Each vector size: {len(doc_vectors[0])}")