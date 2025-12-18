Contract Answerer 📄🤖

AI powered contract and policy question answering system

Contract Answerer is a retrieval augmented generation application that allows users to ask natural language questions about legal contracts and collective bargaining agreements and receive accurate, source grounded answers.

Built as a portfolio project to demonstrate real world AI system design, document retrieval, and end to end application development.

🚀 Why This Project

Legal and employment contracts are long, technical, and difficult to navigate. Finding answers to simple questions often requires reading hundreds of pages or consulting experts.

Contract Answerer solves this by combining semantic search and large language models to deliver fast, reliable answers grounded in the original contract text.

This mirrors the architecture used in enterprise knowledge bases and internal search tools.

✨ Features

• Natural language Q and A over PDF contracts
• Semantic search using vector embeddings
• Retrieval augmented generation to reduce hallucinations
• Chat based web interface for non technical users
• Modular ingestion pipeline for adding new documents

🧠 How It Works

Contract PDFs are ingested and split into text chunks

Chunks are converted into embeddings

Embeddings are stored in a vector database

User questions are embedded and matched semantically

Relevant contract sections are retrieved

The LLM generates an answer using only retrieved content

This approach keeps responses accurate, explainable, and traceable.

🛠️ Tech Stack

• Python
• Streamlit for the web interface
• LangChain for LLM orchestration
• ChromaDB for vector storage
• OpenAI embeddings and language models
• PDF parsing utilities

📁 Project Structure

app.py
Main Streamlit application handling UI, chat flow, and response generation.

load.py
Document ingestion pipeline including PDF loading, chunking, embeddings, and storage.

Contracts/
Folder containing PDF contracts used by the application.

env/
Python virtual environment for dependency isolation.

💬 Example Questions

• What happens if my position is reclassified
• What is the remote work policy
• How much notice is required before a layoff
• What benefits am I entitled to under this agreement

🏃‍♂️ Running Locally

Clone the repository

Create and activate a Python virtual environment

Install dependencies from requirements.txt

Set your OpenAI API key as an environment variable

Run the app with Streamlit

streamlit run app.py

🎯 What This Demonstrates

• End to end RAG system design
• Working with unstructured document data
• Vector databases and semantic retrieval
• Prompt engineering and grounding strategies
• Building user facing AI applications

This architecture is directly applicable to HR tools, internal documentation search, policy engines, and enterprise AI assistants.

🔮 Future Improvements

• Inline citations with highlighted source text
• Multi document and multi contract querying
• Authentication and access control
• Answer confidence scoring and evaluation

👤 About the Author

Abdallah Elhamawi
MS Software Development candidate at Boston University
Focused on applied AI, software engineering, and ethical AI systems
