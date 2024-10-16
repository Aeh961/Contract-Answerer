import streamlit as st
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader
import os
import chromadb



def load_chunk_persist_pdf() -> Chroma:
    OPENAI_API_KEY=""
    pdf_folder_path =os.path.abspath("C:\\Users\\abdal\\OneDrive\\Desktop\\PROTEC17 QA\\Contracts")
    documents = []
    for file in os.listdir(pdf_folder_path):
        if file.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder_path, file)
            loader = PyPDFLoader(pdf_path)
            documents.extend(loader.load())
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
    chunked_documents = text_splitter.split_documents(documents)
    client = chromadb.Client()
    if client.list_collections():
        consent_collection = client.create_collection("consent_collection")
    else:
        print("Collection already exists")
    vectordb = Chroma.from_documents(
        documents=chunked_documents,
        embedding=OpenAIEmbeddings(openai_api_key= OPENAI_API_KEY),
        persist_directory=os.path.abspath("C:\\Users\\abdal\\OneDrive\Desktop\PROTEC17 QA\\chromastore")
    )
    vectordb.persist()
    return vectordb


if __name__ == "__main__":
    load_chunk_persist_pdf()