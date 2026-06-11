from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from pathlib import Path

current_dir = Path(__file__).parent  # embeddings folder
loader = TextLoader(str(current_dir / "myfile.txt"))  # embeddings/myfile.txt ✅
# loader=TextLoader("myfile.txt")
documents=loader.load()

text_splitter=CharacterTextSplitter(chunk_size=100,chunk_overlap=30)
docs=text_splitter.split_documents(documents)

embeddings =OllamaEmbeddings()
db=FAISS.from_documents(docs,embeddings)
db

