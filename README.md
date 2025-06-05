# BharatBot--AI-Legal-Assistant
The BharatBot can answer based on your specific document that you have uplaoded.This bot has been created with RAG
BharatBot – RAG-Powered AI Legal Assistant
BharatBot is a Streamlit web app that allows users to upload legal PDFs and ask questions about them using a powerful Retrieval-Augmented Generation (RAG) architecture, powered by Cohere LLMs and LangChain.

Features
Upload any legal PDF (e.g., Constitution, Acts, Judgments)

Ask natural language questions based on the document

Get answers with source document references

Uses vector embeddings + retrieval + generation

Powered By
LangChain – for document loading, chunking, vector search, and QA chains

Cohere LLMs – command-r model for legal question-answering

FAISS – for semantic vector search

RAG (Retrieval-Augmented Generation) – combines document knowledge with LLM reasoning

Libraries & Tools Used
streamlit – Interactive web UI

cohere – LLM & embedding API client

langchain – Framework for document QA

faiss – Efficient vector store

dotenv, os, tempfile – Secure config & file handling
