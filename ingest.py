import os
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from langchain_community.embeddings import SentenceTransformerEmbeddings

from langchain_community.document_loaders import PyPDFLoader 

DOCS_DIR = "docs"
if not os.path.exists(DOCS_DIR):
    os.makedirs(DOCS_DIR)

print("📌 Loading and parsing documents (Markdown & PDF)...")

documents = []


for file_name in os.listdir(DOCS_DIR):
    file_path = os.path.join(DOCS_DIR, file_name)
    
   
    if file_name.endswith(".md"):
        with open(file_path, "r", encoding="utf-8") as f:
            text_content = f.read()
            if text_content.strip(): 
                documents.append(Document(page_content=text_content, metadata={"source": file_name}))
                
   
    elif file_name.endswith(".pdf"):
        try:
            loader = PyPDFLoader(file_path)
            pdf_docs = loader.load() 
            documents.extend(pdf_docs)
            print(f"✅ Successfully loaded PDF file: {file_name}")
        except Exception as e:
            print(f"❌ Error loading PDF {file_name}: {e}")

print(f"📊 Total files found and loaded in memory: {len(documents)}")

if len(documents) == 0:
    print(f"❌ Error: No text or PDF found inside files in '{DOCS_DIR}'!")
    exit()


text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)
print(f"📊 Total chunks created: {len(chunks)}")

print("📌 Generating Embeddings using Sentence-Transformers directly...")

embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

print("📌 Building and saving FAISS Vector Database...")
db = FAISS.from_documents(chunks, embeddings)
db.save_local("faiss_index")

print("✅La base de donnees a ete cree et enregistree avec succes a partir de fichiers MD et PDF et associee à l'email !")
