import streamlit as st
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain


st.title("🤖 Chatbot Support Technique - Niveau 1")
st.write("Posez vos questions basées sur la documentation confidentielle de l'entreprise.")


embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
retriever = db.as_retriever(search_kwargs={"k": 3})


llm = Ollama(model="llama3.2")


system_prompt = (
    "You are a helpful, respectful, and honest virtual assistant, acting exactly like ChatGPT.\n"
    "1. Always respond to the user in the SAME language they use (Arabic, French, or English) with perfect grammar and fluency. Do not mix languages.\n"
    "2. For general conversation, casual talk, or any topic outside company rules, answer freely and intelligently using your own vast internal knowledge base.\n"
    "3. Only use the context below if the user asks a specific technical question about company guidelines.\n\n"
    "Context:\n{context}"
)




prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])


question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_query := st.chat_input("Comment puis-je vous aider ?"):
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        with st.spinner("Réflexion..."):
          
            response = rag_chain.invoke({"input": user_query})
            answer = response["answer"]
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
