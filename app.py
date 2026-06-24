import streamlit as st
from pypdf import PdfReader
import requests

st.title("AI Document Assistant")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    st.success("PDF Loaded Successfully!")

    if st.button("Summarize"):
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen3:8b",
                "prompt": f"Summarize this document:\n\n{text[:10000]}",
                "stream": False
            }
        )

        st.write(response.json()["response"])

    question = st.text_input("Ask a question about the document")

    if question:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen3:8b",
                "prompt": f"Document:\n{text[:3000]}\n\nQuestion: {question}",
                "stream": False
            }
        )

        st.write(response.json()["response"])