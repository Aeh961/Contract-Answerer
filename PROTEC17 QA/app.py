import streamlit as st
import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

# Load key (must be set in terminal)
if not os.environ.get("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not set. Run: export OPENAI_API_KEY='your_key'")

persist_directory = "chromastore"

def generate_response(query_text):
    # Load vector DB
    embeddings = OpenAIEmbeddings()
    db = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )

    retriever = db.as_retriever()

    # LLM
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    # RetrievalQA chain
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )

    return qa.run(query_text)


# ----- Streamlit UI -----

st.set_page_config(page_title="PROTEC17 Contract AI", layout="centered")
st.title("PROTEC17 Contract AI Assistant")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
user_query = st.chat_input("Ask a contract question...")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)

    answer = generate_response(user_query)

    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.chat_message("assistant").write(answer)
