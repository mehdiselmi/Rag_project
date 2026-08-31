import os
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.document_loaders import PyPDFLoader
 

# 1. Définition du dossier contenant les documents sources

DOCS_DIR = "docs"
 
# Création du dossier s'il n'existe pas encore 
if not os.path.exists(DOCS_DIR):
    os.makedirs(DOCS_DIR)
 
print("📌 Chargement et analyse des documents (Markdown et PDF)...")
 
documents = [] 
 
 

# 2. Lecture de tous les fichiers du dossier "docs"

for file_name in os.listdir(DOCS_DIR):
    file_path = os.path.join(DOCS_DIR, file_name)
 
    #  fichier Markdown
    if file_name.endswith(".md"):
        with open(file_path, "r", encoding="utf-8") as f:
            text_content = f.read()
            if text_content.strip():  # Ignore les fichiers vides
                
                documents.append(Document(page_content=text_content, metadata={"source": file_name}))
 
    # fichier PDF 
    elif file_name.endswith(".pdf"):
        try:
            loader = PyPDFLoader(file_path)
            pdf_docs = loader.load()  
            documents.extend(pdf_docs)
            print(f"✅ Fichier PDF chargé avec succès : {file_name}")
        except Exception as e:
            print(f"❌ Erreur lors du chargement du PDF {file_name} : {e}")
 
print(f"📊 Nombre total de fichiers trouvés et chargés en mémoire : {len(documents)}")
 
# Arrêt du script si aucun document n'a été trouvé
if len(documents) == 0:
    print(f"❌ Erreur : aucun texte ni PDF trouvé dans le dossier '{DOCS_DIR}' !")
    exit()
 
 

# 3. Découpage des documents en fragments (Chunks)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=40)
chunks = text_splitter.split_documents(documents)
print(f"📊 Nombre total de fragments (chunks) créés : {len(chunks)}")
 
 

# 4. Conversion de chaque fragment en vecteur (Embedding)

print("📌 Génération des embeddings avec Sentence-Transformers...")

embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
 
 

# 5. Construction et sauvegarde de la base vectorielle FAISS

print("📌 Construction et sauvegarde de la base vectorielle FAISS...")
 
# FAISS.from_documents effectue automatiquement :

db = FAISS.from_documents(chunks, embeddings)
 
# Sauvegarde locale de l'index, afin de ne pas avoir à le reconstruire

db.save_local("faiss_index")
 
print("✅ La base de données a été créée et enregistrée avec succès à partir des fichiers Markdown et PDF, conformément au projet !")
 