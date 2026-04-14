from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

documents = [
    "fleet executive road pe delivery karta hai",
    "software engineer code likhta hai",
    "data scientist ML models banata hai",
    "Zomato aur Swiggy food delivery apps hain",
    "Paytm ek payment gateway hai",
    "machine learning data se seekhta hai"
]

# ✅ ChromaDB banao - automatically persist hota hai!
vectorstore = Chroma.from_texts(
    documents, 
    embeddings,
    persist_directory="./chroma_db"  # disk pe save
)

# ✅ Search karo
query = "delivery job kya hoti hai"
results = vectorstore.similarity_search_with_score(query, k=3)

print(f"Query: {query}")
print("\n--- Top 3 Results ---")
for i, (doc, score) in enumerate(results):
    print(f"\nRank {i+1}: {doc.page_content}")
    print(f"Score: {score:.4f}")

# ✅ Retriever banao - RAG pipeline ka actual component!
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
docs = retriever.invoke("food delivery app")
print("\n--- Retriever Results ---")
for doc in docs:
    print(doc.page_content)