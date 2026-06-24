This project is an AI-powered document assistant that allows users to upload PDF files and interact with them using natural language.
It uses Ollama (local LLMs) to summarize content and answer questions based on the uploaded document.
The system extracts text from PDFs, processes it locally, and sends a trimmed context to an AI model for intelligent responses.

How It Works
User uploads a PDF file
Text is extracted using PyPDF2
Only a portion of text (e.g. first 3000 characters) is sent to the model
User asks a question about the document
Prompt is sent to Ollama (qwen3:8b model)
AI generates:
Summary
Answer based on document context

Tech Stack
Python 
Streamlit
PyPDF2
Ollama (Local LLM runtime)
Qwen3:8B model

Features
 Upload and read PDF documents
 Ask questions about document content
 Extracts and processes text automatically
 Uses local AI (Ollama) for responses
 Fully offline after setup (no cloud API required)
 Simple Streamlit web interface
