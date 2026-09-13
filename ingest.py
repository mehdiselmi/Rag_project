import os
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader


#1  les documents source
DOCS_DIR = "docs"

if not os.path.exists(DOCS_DIR):
    os.makedirs(DOCS_DIR)

print("📌 Chargement et analyse des documents (Markdown et PDF)...")

documents = []

#2 Lecture de tous les fichiers 
for file_name in os.listdir(DOCS_DIR):
    file_path = os.path.join(DOCS_DIR, file_name)

    #2.1 fichiers Markdown
    if file_name.endswith(".md"):
        with open(file_path, "r", encoding="utf-8") as f:
            text_content = f.read()
            if text_content.strip():
                documents.append(Document(page_content=text_content, metadata={"source": file_name}))

    #2.2 fichiers PDF
    elif file_name.endswith(".pdf"):
        try:
            loader = PyPDFLoader(file_path)
            pdf_docs = loader.load()
            documents.extend(pdf_docs)
            print(f"✅ Fichier PDF chargé avec succès : {file_name}")
        except Exception as e:
            print(f"❌ Erreur lors du chargement du PDF {file_name} : {e}")

print(f" Nombre total de fichiers trouvés et chargés en mémoire : {len(documents)}")

if len(documents) == 0:
    print(f"❌ Erreur : aucun texte ni PDF trouvé dans le dossier '{DOCS_DIR}' !")
    exit()

#3 Découpage des documents 
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)
print(f" Nombre total de chunks créés : {len(chunks)}")

#4 Génération des embeddings 
print("📌 Génération des embeddings avec Sentence-Transformers...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

#5 Construction de la base vectorielle FAISS et sauvegarde locale
print("📌 Construction et sauvegarde de la base vectorielle FAISS...")
db = FAISS.from_documents(chunks, embeddings)
db.save_local("faiss_index")

print("✅ La base de données a été créée et enregistrée avec succès à partir des fichiers Markdown et PDF, conformément au projet !")