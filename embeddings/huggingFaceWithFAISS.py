from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Documents
documents = [
    "fleet executive road pe delivery karta hai",
    "software engineer code likhta hai",
    "data scientist ML models banata hai",
    "Zomato aur Swiggy food delivery apps hain",
    "Paytm ek payment gateway hai",
    "machine learning data se seekhta hai"
]

# ✅ FAISS vector store banao - embed + store ek saath!
vectorstore = FAISS.from_texts(documents, embeddings)

# ✅ Similar documents dhundo
query = "delivery job kya hoti hai"
results = vectorstore.similarity_search(query, k=3)

print(f"Query: {query}")
print("\n--- Top 3 Results ---")
for i, doc in enumerate(results):
    print(f"\nRank {i+1}: {doc.page_content}")





# Score ke saath results
results = vectorstore.similarity_search_with_score(query, k=3)

print(f"Query: {query}")
print("\n--- Top 3 Results with Score ---")
for i, (doc, score) in enumerate(results):
    print(f"\nRank {i+1}: {doc.page_content}")
    print(f"Score: {score:.4f}  ← lower = more similar!")

# ✅ FAISS save karo disk pe!
vectorstore.save_local("faiss_index")
print("\n✅ FAISS index saved!")

# ✅ Wapas load karo
loaded_vs = FAISS.load_local(
    "faiss_index", 
    embeddings,
    allow_dangerous_deserialization=True
)
results2 = loaded_vs.similarity_search("food delivery app", k=2)
print("\n--- Loaded FAISS Results ---")
for doc in results2:
    print(doc.page_content)