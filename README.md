# Contract Answerer

An AI powered document question answering application that allows users to ask natural language questions about long PDF documents and receive accurate, source grounded answers.

This project demonstrates a production minded implementation of retrieval augmented generation using modern LLM tooling.

## Demo
90 second walkthrough and setup video: <link here>

## Why this project matters
Many real world workflows depend on large and complex documents that are difficult to search or reason about manually. This project explores how large language models, embeddings, and vector search can be combined to make long form documents immediately useful while minimizing hallucinations.

## Key features
1. Ask natural language questions over arbitrary PDF documents
2. Embeddings based retrieval for precise context selection
3. Context constrained LLM responses to improve accuracy
4. Simple and fast UI designed for iteration and experimentation

## Tech stack
1. Python
2. Streamlit
3. OpenAI API
4. ChromaDB
5. LangChain

## Quickstart two minutes

Step 1 Clone the repository

    git clone https://github.com/Aeh961/Contract-Answerer.git
    cd Contract-Answerer

Step 2 Create and activate a virtual environment

    python -m venv .venv
    source .venv/bin/activate

Step 3 Install dependencies

    pip install -r requirements.txt

Step 4 Add your documents

    mkdir -p data/contracts

Place any PDF files you want to query into the data contracts folder.

Step 5 Set your API key

    export OPENAI_API_KEY="your_key_here"

Step 6 Run the application

    streamlit run src/app.py

## How it works
1. PDF documents are loaded and split into semantic chunks
2. Each chunk is embedded and stored in a vector database
3. User questions retrieve the most relevant chunks
4. The language model generates answers using only retrieved context

## Project structure

    src
      app.py          Streamlit application
      load.py         Document ingestion and embedding
    data
      contracts       User provided PDFs
    README.md
    requirements.txt

## Future improvements
1. Inline citations with highlighted source text
2. Streaming responses for improved user experience
3. Document metadata filtering
4. Cost and latency optimizations

## Author
Built by Abdallah Elhamawi as part of a broader exploration into practical and reliable AI systems.
