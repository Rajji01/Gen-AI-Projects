from langchain_community.document_loaders import TextLoader
from pathlib import Path

# Current file ka location
current_dir = Path(__file__).parent
file_path = current_dir / "myfile.txt"  # Dataingestion/myfile.txt

print(f"Looking for file at: {file_path.absolute()}")

if file_path.exists():
    loader = TextLoader(str(file_path), encoding="utf-8")
    docs = loader.load()
    print(docs[0].page_content)
else:
    print(f"❌ File nahi mili: {file_path}")