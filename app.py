import streamlit as st
import os
import subprocess
import sys
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

DOCS_DIR = "docs"
if not os.path.exists(DOCS_DIR):
    os.makedirs(DOCS_DIR)


#1 gestion des documents 
with st.sidebar:
    st.subheader("📂 Ajouter un document")

    uploaded_file = st.file_uploader(
        "Choisissez un fichier (.md ou .pdf)",
        type=["md", "pdf"]
    )

    if uploaded_file is not None:
        save_path = os.path.join(DOCS_DIR, uploaded_file.name)
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"✅ '{uploaded_file.name}' ajouté !")

        if st.button("🔄 Reconstruire la base"):
            with st.spinner("Reconstruction en cours..."):
                result = subprocess.run(
                    [sys.executable, "ingest.py"],
                    capture_output=True,
                    text=True
                )

                if result.returncode == 0:
                    st.cache_resource.clear()
                    st.success("✅ Base reconstruite ")
                    st.rerun()
                else:
                    st.error("❌ Erreur :")
                    st.text(result.stderr)

   

    st.divider()
    if st.button("🔄 Nouvelle conversation"):
        st.session_state.messages = []
        st.rerun()


#2 Titre
st.title("🤖 Chatbot Support Technique - Niveau 1")
st.write("Posez vos questions basées sur la documentation confidentielle de l'entreprise.")


# Chargement de la base de connaissances (FAISS)
@st.cache_resource
def load_database():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    return db

db = load_database()
retriever = db.as_retriever(search_kwargs={"k": 3})


#3  Modèle de langage
@st.cache_resource
def load_llm():
    return ChatOpenAI(
        model="openrouter/free",
        openai_api_base="https://openrouter.ai/api/v1",
        openai_api_key=os.environ.get("OPENROUTER_API_KEY"),
        temperature=0.2
    )

llm = load_llm()

#4 Instructions données au modèle
system_prompt = (
    "Tu es un assistant virtuel spécialisé.\n\n"
    "Consignes :\n"
    "1. Réponds uniquement en utilisant les informations présentes dans le contexte ci-dessous.\n"
    "2. Si la question ne concerne pas directement la documentation ou si l'information est absente du contexte, réponds simplement : 'Désolé, je ne trouve pas cette information dans la documentation.'\n"
    "3. Ne donne jamais de réponses basées sur tes propres connaissances générales.\n"
    "4. Réponds toujours dans la même langue que l'utilisateur.\n\n"
    "Contexte :\n{context}"
)


prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

#5 Construction de la chaîne complète 
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

#6 Historique de la conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#7  Génération de la réponse
if user_query := st.chat_input("Comment puis je vous aider ?"):
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        with st.spinner("Réflexion en cours..."):
            response = rag_chain.invoke({"input": user_query})
            answer = response["answer"]
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})