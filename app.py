
import streamlit as st
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
 
# Outils reliant la recherche (retriever) à la génération de réponse (LLM)
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
 
 

# 1. Titre et description de l'interface

st.title("🤖 Chatbot Support Technique - Niveau 1")
st.write("Posez vos questions basées sur la documentation confidentielle de l'entreprise.")
 

# 2. Chargement de la base FAISS (connaissances déjà indexées)

@st.cache_resource
def load_database():
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    return db

db = load_database()

retriever = db.as_retriever(search_kwargs={"k": 2})
 
 

# 3. Configuration du LLM (modèle de langage local)

@st.cache_resource
def load_llm():
    return Ollama(
        model="llama3.2",
        keep_alive=-1,     
        num_ctx=2048,
        num_thread=4
    )
 
llm = load_llm()

# 4. Instruction (prompt) envoyée au modèle


system_prompt = (
    "Tu es un assistant virtuel serviable, respectueux et honnête, qui agit exactement comme ChatGPT.\n"
    "1. Réponds toujours à l'utilisateur dans la MÊME langue qu'il utilise (arabe, français ou anglais), avec une grammaire et une fluidité parfaites. Ne mélange pas les langues.\n"
    "2. Pour les conversations générales, les échanges informels ou tout sujet en dehors des règles de l'entreprise, réponds librement et intelligemment en utilisant tes propres connaissances internes.\n"
    "3. N'utilise le contexte ci-dessous que si l'utilisateur pose une question technique spécifique liée aux consignes de l'entreprise.\n\n"
    "Contexte :\n{context}"
)
 
# Construction du modèle de conversation : instruction système + message utilisateur
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])
 
 
# 5. Construction de la chaîne complète (RAG Chain)


question_answer_chain = create_stuff_documents_chain(llm, prompt)
 

rag_chain = create_retrieval_chain(retriever, question_answer_chain)
 
 

# 6. Gestion de l'historique de conversation

 
# Initialisation de la mémoire de session si elle n'existe pas encore
if "messages" not in st.session_state:
    st.session_state.messages = []
 
# Affichage de l'ensemble des messages précédents de la session en cours
for message in st.session_state.messages:
    with st.chat_message(message["role"]):  # "role" = user ou assistant
        st.markdown(message["content"])
 
 

# 7. Réception d'une nouvelle question et génération de la réponse

 
# Zone de saisie en bas de page, déclenchée à la validation de la question
if user_query := st.chat_input("Comment puis-je vous aider ?"):
 
    # Ajout de la question à l'historique, puis affichage
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)
 
    # Génération de la réponse
    with st.chat_message("assistant"):
        with st.spinner("Réflexion en cours..."):
 
            # Exécution de la chaîne complète : recherche FAISS + génération via Ollama
            response = rag_chain.invoke({"input": user_query})
            answer = response["answer"]
 
            # Affichage de la réponse et ajout à l'historique de la session
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
 