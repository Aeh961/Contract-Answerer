Contract Answerer

Contract Answerer is an AI powered application that enables users to ask natural language questions about legal contracts and collective bargaining agreements and receive accurate, source grounded answers in seconds.

The project demonstrates real world use of retrieval augmented generation to make long, complex PDF documents searchable, explainable, and usable for non legal audiences.

Problem This Solves

Legal and employment contracts are often hundreds of pages long and difficult to interpret. Finding answers to simple questions like eligibility, benefits, or policy rules requires significant time and expertise.

Contract Answerer reduces this friction by combining semantic search and large language models to deliver fast, reliable answers tied directly to the source document.

Key Capabilities

Natural language Q and A over PDF contracts

Semantic search using vector embeddings

Retrieval augmented generation to reduce hallucinations

Chat based web interface for non technical users

Modular design that supports adding new documents easily

System Architecture

PDF contracts are ingested and split into chunks

Each chunk is converted into embeddings

Embeddings are stored in a vector database

User queries are embedded and matched semantically

Relevant contract sections are retrieved

The LLM generates an answer grounded in retrieved text

This mirrors production grade RAG systems used in enterprise search and internal knowledge tools.

Tech Stack

Python

Streamlit for frontend and interaction

LangChain for LLM orchestration

ChromaDB for vector storage

OpenAI embeddings and language models

PDF parsing libraries

Code Overview

app.py
Handles the Streamlit UI, chat interaction, and answer generation pipeline.

load.py
Manages document ingestion, chunking, embedding creation, and storage in ChromaDB.

Contracts directory
Houses PDF contract files used by the application.

Example Questions It Can Answer

What happens if my role is reclassified

What is the remote work policy

How much notice is required before a layoff

What benefits am I entitled to under this agreement

Why This Matters to Employers

This project demonstrates hands on experience with:

Designing and implementing RAG systems

Working with unstructured data at scale

Building end to end AI applications

Applying prompt engineering and retrieval strategies

Creating user friendly interfaces for complex systems

The same architecture applies to internal knowledge bases, policy search tools, HR systems, and enterprise document search products.

Future Enhancements

Inline citations and highlighted source text

Multi document and multi contract querying

Authentication and role based access

Improved evaluation and answer confidence scoring

About Me

Abdallah Elhamawi
MS Software Development candidate at Boston University
Interested in AI powered systems, applied machine learning, and building products that improve access to information

If you want, I can also:

Rewrite this to match a specific job posting

Add a short Architecture section with a diagram description

Create a one paragraph project blurb for resumes and LinkedIn

Optimize this for ATS keyword scanning
