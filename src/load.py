import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# Your API key must already be exported in the terminal:
# export OPENAI_API_KEY="sk-proj-xxxx"

def load_chunk_persist_pdf():

    pdf_files = [
        "Contracts/PROTEC17-Municipal-Court-CBA-2023-2026-FINAL.pdf",
        "Contracts/PROTEC17-Seattle-Main-Executive-CBA-23-26-FINAL.pdf",
        "Contracts/Supervisors-2021-2024.pdf"
    ]

    all_docs = []

    # Load all PDFs
    for pdf_path in pdf_files:
        print(f"Loading: {pdf_path}")
        loader = PyPDFLoader(pdf_path)
        docs = loader.load()
        all_docs.extend(docs)

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    split_docs = text_splitter.split_documents(all_docs)
    print(f"Total chunks created: {len(split_docs)}")

    # Create embeddings and store in Chroma
    persist_dir = "chromastore"
    embeddings = OpenAIEmbeddings()

    vectordb = Chroma.from_documents(
        documents=split_docs,
        embedding=embeddings,
        persist_directory=persist_dir
    )

    vectordb.persist()
    print(f"Vector store created at: {persist_dir}")


if __name__ == "__main__":
    load_chunk_persist_pdf()
