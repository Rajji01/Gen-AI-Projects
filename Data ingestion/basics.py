from langchain_community.document_loaders import TextLoader
from pathlib import Path

# # Current file ka location
# current_dir = Path(__file__).parent
# file_path = current_dir / "myfile.txt"  # Dataingestion/myfile.txt

# print(f"Looking for file at: {file_path.absolute()}")

# if file_path.exists():
#     loader = TextLoader(str(file_path), encoding="utf-8")
#     docs = loader.load()
#     print(docs[0].page_content)
# else:
#     print(f"❌ File nahi mili: {file_path}")


# from langchain_community.document_loaders import PyPDFLoader
# from pathlib import Path

# # Current directory mein "sample.pdf" naam ki file rakho
# current_dir = Path(__file__).parent
# pdf_path = current_dir / "sample.pdf"

# # Check karo file hai ya nahi
# if pdf_path.exists():
#     loader = PyPDFLoader(str(pdf_path))
#     docs = loader.load()
    
#     print(f"✅ PDF loaded successfully!")
#     print(f"Total pages: {len(docs)}")
#     print(f"\n--- Page 1 Content ---")
#     print(docs[0].page_content[:500])  # pehle 500 characters
#     print(f"\n--- Metadata ---")
#     print(docs[0].metadata)
#     print(type(docs[0]))
# else:
#     print(f"❌ File not found: {pdf_path}")


import os
os.environ["USER_AGENT"] = "MyRAGApp/1.0"

from langchain_community.document_loaders import WebBaseLoader
import bs4

loader = WebBaseLoader(
    web_paths=["https://en.wikipedia.org/wiki/Artificial_intelligence"],
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            "div",
            attrs={"id": "mw-content-text"}  # Wikipedia ka main content div
        )
    )
)

docs = loader.load()
print(f"Content length: {len(docs[0].page_content)}")
print(docs[0].page_content[:500])



# import os
# os.environ["USER_AGENT"] = "MyRAGApp/1.0"

# from langchain_community.document_loaders import ArxivLoader

# loader = ArxivLoader(
#     query="1706.03762",
#     load_max_docs=1,
#     load_all_available_meta=True,
#     doc_content_chars_max=2000  # sirf abstract level content
# )

# docs = loader.load()

# print(f"Title: {docs[0].metadata.get('Title')}")
# print(f"Authors: {docs[0].metadata.get('Authors')}")
# print(f"Published: {docs[0].metadata.get('Published')}")
# print(f"\nContent preview:\n{docs[0].page_content[:500]}")




from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

# ❌ Wrong - Document objects pass kar raha tha
# text_splitter.create_documents(docs)

# ✅ Correct - Already Document objects hain, split_documents use karo
chunks = text_splitter.split_documents(docs)

print(f"Total chunks: {len(chunks)}")
print(f"\n--- Chunk 1 ---")
print(chunks[0].page_content)
print(f"\n--- Chunk 2 ---")
print(chunks[1].page_content)





from langchain_community.document_loaders import TextLoader
from pathlib import Path

# Sahi path do
current_dir = Path(__file__).parent
loader = TextLoader(str(current_dir / 'myfile.txt'))
docs = loader.load()

from langchain_text_splitters import CharacterTextSplitter
text_splitter = CharacterTextSplitter(separator="\n\n", chunk_size=100, chunk_overlap=20)
chunks = text_splitter.split_documents(docs)

print(f"Total chunks: {len(chunks)}")
for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ---")
    print(chunk.page_content)







from langchain_text_splitters import HTMLHeaderTextSplitter

html_content = """
<html>
<body>
    <h1>Artificial Intelligence</h1>
    <p>AI is the simulation of human intelligence by machines.</p>
    
    <h2>Machine Learning</h2>
    <p>ML is a subset of AI that learns from data automatically.</p>
    
    <h3>Deep Learning</h3>
    <p>Deep Learning uses neural networks with many layers.</p>
    
    <h2>Natural Language Processing</h2>
    <p>NLP helps computers understand human language like Hindi and English.</p>
    
    <h3>Large Language Models</h3>
    <p>LLMs like GPT and Claude are trained on massive text data.</p>
</body>
</html>
"""

# Konse headers pe split karna hai
headers_to_split_on = [
    ("h1", "Header 1"),
    ("h2", "Header 2"),
    ("h3", "Header 3"),
]

splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
chunks = splitter.split_text(html_content)

print(f"Total chunks: {len(chunks)}")
for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ---")
    print(f"Content: {chunk.page_content}")
    print(f"Metadata: {chunk.metadata}")





import json
import requests

json_data=requests.get("https://api.smith.langchain.com/openapi.json").json()

from langchain_text_splitters import RecursiveJsonSplitter
json_splitter=RecursiveJsonSplitter(max_chunk_size=300)
json_chunks=json_splitter.split_json(json_data)

for chunk in json_chunks[:3]:
    print(chunk)

docs=json_splitter.create_documents(texts=[json_data])
for doc in docs[:3]:
    print(doc)